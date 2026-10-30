"""Scenario timeline: scenario.md -> one self-contained HTML (images inlined).

Usage: python build_timeline.py <scenario.md> [-o <out.html>]
Default output: <scenario>-timeline.html next to the md. Markdown format: example.md next to this script.
"""
import argparse, base64, html, io, os, re, shutil, struct, subprocess, sys, tempfile

E = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))

IMG = re.compile(r'^!\[([^\]]*)\]\((?:<(.+?)>|(\S+?))(?:\s+"(.+?)")?\)$')
SCENE = re.compile(r'^\*\*(\d+(?:[.,]\d+)?)\s*[–-]\s*(\d+(?:[.,]\d+)?)\s*(?:s|sec)\.?(.*?)\*\*\s*(.*)$')
CAP = {"caption", "title", "subtitle"}
NOTE = {"screen", "screens", "note", "sound", "music"}


def inline(s):
    s = E(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return re.sub(r"(\[[^\]]+\])", r"<mark>\1</mark>", s)


def num(s):
    return float(s.replace(",", "."))


def fmt(x):
    return ("%g" % x)


def img_size(data):
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            m = data[i + 1]
            if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP" and data[12:16] == b"VP8X":
        return 1 + int.from_bytes(data[24:27], "little"), 1 + int.from_bytes(data[27:30], "little")
    return 16, 9


def encode(path):
    """(w, h, mime, base64): JPEG up to 900 px wide (600 for portrait) via PIL or macOS sips, else the file as is."""
    raw = open(path, "rb").read()
    w, h = img_size(raw)
    lim = 900 if w > h else 600
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        if im.width > lim:
            im = im.resize((lim, round(im.height * lim / im.width)), Image.LANCZOS)
        b = io.BytesIO()
        im.save(b, "JPEG", quality=80, optimize=True, progressive=True)
        return im.width, im.height, "image/jpeg", base64.b64encode(b.getvalue()).decode()
    except ImportError:
        pass
    if shutil.which("sips"):
        with tempfile.TemporaryDirectory() as td:
            out = os.path.join(td, "x.jpg")
            r = subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "80", "--resampleWidth",
                                str(min(lim, w)), path, "--out", out], capture_output=True)
            if r.returncode == 0 and os.path.exists(out):
                data = open(out, "rb").read()
                w2, h2 = img_size(data)
                return w2, h2, "image/jpeg", base64.b64encode(data).decode()
    print("no PIL or sips: %s inlined full size" % os.path.basename(path), file=sys.stderr)
    ext = os.path.splitext(path)[1].lower().lstrip(".")
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp", "gif": "image/gif"}.get(ext, "image/png")
    return w, h, mime, base64.b64encode(raw).decode()


def parse(lines, base):
    doc = {"title": "", "head": [], "sections": []}
    imgs = {}  # key path -> {"cls", "path", "name"}
    cur, mode, block = None, "head", None

    def reg(path, name):
        p = path if os.path.isabs(path) else os.path.join(base, path)
        if p not in imgs:
            if not os.path.exists(p):
                print("no image:", p, file=sys.stderr)
                return None
            imgs[p] = {"cls": "im%d" % len(imgs), "path": p, "name": name or os.path.basename(p)}
        return p

    for ln in lines:
        if ln.startswith("# ") and not doc["title"]:
            doc["title"] = ln[2:].strip()
            continue
        if ln.startswith("## "):
            cur = {"title": ln[3:].strip(), "intro": [], "scenes": [], "after": [], "blocks": []}
            doc["sections"].append(cur)
            mode = "intro"
            continue
        if ln.startswith("### ") and cur:
            block = {"title": ln[4:].strip(), "items": []}
            cur["blocks"].append(block)
            mode = "block"
            continue
        if not ln.strip():
            continue
        if mode == "head":
            doc["head"].append(ln.strip())
            continue
        m = IMG.match(ln.strip())
        if m:
            alt, p1, p2, cap = m.groups()
            key = reg(p1 or p2, cap or alt)
            if key:
                if mode == "scene":
                    cur["scenes"][-1]["imgs"].append(key)
                elif mode == "intro":
                    cur["intro"].append(("img", key))
                else:
                    block["items"].append(("img", key))
            continue
        if mode == "block":
            block["items"].append(("li", ln[2:]) if ln.startswith("- ") else ("p", ln))
            continue
        m = SCENE.match(ln)
        if m:
            a, b, lab, act = m.groups()
            cur["scenes"].append({"a": num(a), "b": num(b), "t": "%s–%s s" % (fmt(num(a)), fmt(num(b))),
                                  "label": lab.strip(" ."), "act": act, "items": [], "imgs": []})
            mode = "scene"
            continue
        if mode == "intro":
            cur["intro"].append(("li", ln[2:]) if ln.startswith("- ") else ("p", ln))
            continue
        sc = cur["scenes"][-1]
        if ln.startswith(("  - ", "    - ")) and sc["items"]:
            sc["items"][-1]["tr"] = ln.strip()[2:].strip()
        elif ln.startswith("- "):
            k, _, v = ln[2:].partition(": ")
            if not v or len(k.split()) > 2:
                k, v = "", ln[2:]
            sc["items"].append({"k": k.strip(), "v": v})
        else:
            cur["after"].append(ln)
    return doc, imgs


def build(md_path, out_path):
    base = os.path.dirname(os.path.abspath(md_path))
    doc, imgs = parse(open(md_path, encoding="utf-8").read().splitlines(), base)
    enc = {k: encode(v["path"]) for k, v in imgs.items()}
    portrait = {k: e[1] > e[0] for k, e in enc.items()}

    def media(keys, cls=""):
        return "".join('<figure class="shot %s"><div class="ph %s" role="img" aria-label="%s"></div>'
                       '<figcaption>%s</figcaption></figure>' % (cls, imgs[k]["cls"], E(imgs[k]["name"]), E(imgs[k]["name"]))
                       for k in keys)

    parts = []
    for si, s in enumerate(doc["sections"]):
        sid = "v%d" % (si + 1)
        total = max([sc["b"] for sc in s["scenes"]] or [1])
        step = 5 if total <= 60 else 10 if total <= 180 else 30 if total <= 600 else 60
        kimgs = [v for k, v in s["intro"] if k == "img"]
        segs, scenes = [], []
        for j, sc in enumerate(s["scenes"]):
            keys = sc["imgs"] or kimgs[:1]
            pt = bool(keys) and all(portrait[k] for k in keys)
            scr = any(not portrait[k] for k in keys)
            w = (sc["b"] - sc["a"]) / total * 100
            segs.append('<a class="seg%s" style="width:%.3f%%" href="#%s-%d" title="%s" aria-label="%s"></a>'
                        % (" scr" if scr else "", w, sid, j, E(sc["t"]), E(sc["t"])))
            items = []
            for it in sc["items"]:
                k = it["k"]
                if k and k.lower() not in NOTE:
                    kind = "cap" if k.lower() in CAP else "vo"
                    none = it["v"].strip().lower() in ("none", "—", "-")
                    tr = '<p class="tr">%s</p>' % inline(it["tr"]) if it.get("tr") else ""
                    items.append('<div class="it k-%s%s"><p class="lbl">%s</p><p class="v">%s</p>%s</div>'
                                 % (kind, " none" if none else "", E(k), inline(it["v"]), tr))
                else:
                    items.append('<p class="note">%s%s</p>' % ((E(k) + ": ") if k else "", inline(it["v"])))
            lab = ' <span class="sl">%s</span>' % E(sc["label"]) if sc["label"] else ""
            md = ('<div class="md%s%s">%s</div>' % (" pt-row" if pt else "", " many" if len(keys) > 1 else "",
                                                   media(keys, "pt" if pt else ""))) if keys else ""
            scenes.append('<li class="sc" id="%s-%d">\n<div class="tm"><span class="t">%s</span></div>\n'
                          '<div class="bd"><h3>%s%s</h3><p class="act">%s</p>\n%s\n%s</div></li>'
                          % (sid, j, E(sc["t"]), E(sc["t"]), lab, inline(sc["act"]),
                             "<div class='its'>%s</div>" % "".join(items) if items else "", md))
        ticks = "".join('<span style="left:%.3f%%">%s</span>' % (t / total * 100, t)
                        for t in range(0, int(total) + 1, step))
        intro = "".join('<p class="%s">%s</p>' % ("lead" if k == "p" else "note", inline(v))
                        for k, v in s["intro"] if k != "img")
        if kimgs:
            intro += '<div class="kf">%s</div>' % media(kimgs, "pt")
        after = "".join('<p class="note foot">%s</p>' % inline(a) for a in s["after"])
        blocks = ""
        for b in s["blocks"]:
            body = "".join('<div class="kf">%s</div>' % media([v], "pt") if k == "img"
                           else '<p class="note">%s</p>' % inline(v) if k == "li" else "<p>%s</p>" % inline(v)
                           for k, v in b["items"])
            blocks += '<details class="kling"><summary>%s</summary><div class="kb">%s</div></details>' % (E(b["title"]), body)
        scale = ('<div class="scale" aria-label="Scale 0–%s s"><div class="bar">%s</div><div class="ticks">%s</div></div>'
                 % (fmt(total), "".join(segs), ticks)) if s["scenes"] else ""
        parts.append('<section class="vid" id="%s">\n<h2>%s</h2>%s\n%s\n<ol class="tl">%s</ol>%s\n%s\n</section>'
                     % (sid, E(s["title"]), intro, scale, "".join(scenes), after, blocks))

    css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    css_imgs = "".join(".%s{background-image:url(data:%s;base64,%s);aspect-ratio:%d/%d}"
                       % (imgs[k]["cls"], e[2], e[3], e[0], e[1]) for k, e in enc.items())
    head = "".join('<p class="%s">%s</p>' % ("offer" if i == 0 else "note", inline(v)) for i, v in enumerate(doc["head"]))
    toc = ('<nav class="toc">%s</nav>' % "".join('<a href="#v%d">%s</a>' % (i + 1, E(s["title"]))
                                                 for i, s in enumerate(doc["sections"]))) if len(doc["sections"]) > 1 else ""
    title = E(doc["title"])
    out = ('<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" '
           'content="width=device-width,initial-scale=1">\n<title>%s</title><style>%s\n%s</style></head><body><main>\n'
           '<header class="top"><h1>%s</h1>%s\n%s</header>\n%s</main></body></html>'
           % (title, css, css_imgs, title, head, toc, "".join(parts)))
    open(out_path, "w", encoding="utf-8").write(out)
    print(out_path, len(out) // 1024, "KB,", len(imgs), "images")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("md")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    build(a.md, a.out or os.path.splitext(a.md)[0] + "-timeline.html")
