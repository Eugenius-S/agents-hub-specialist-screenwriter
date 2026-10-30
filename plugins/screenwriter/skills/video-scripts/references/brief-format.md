# Video script: the format for moviemaker

## Header
- Video: <product, title>
- Format: 16:9 first (9:16 after a "yes" on 16:9), duration: <N s>
- Goal and platform: <ad where / demo>, CTA: <exact phrase>
- Video folder: <full path where the After Effects project and sources live>
- Reference: <link or path>: what to take from it (pace, transitions, font), what not

## Sources (real only)
- Interface: <design-tool link with a node id / HTML mockup / screen recording>: which screens and states
- Illustrations and icons: <the style, ids or links>
- Voice-over: <file or "needed, the voice is such and such">, music: <file / "pick, tempo N BPM, mood">
- Logo, end card: <file>

## Scenes
| # | Time | On screen (what and from where, from which source) | Motion / transition | Voice-over (verbatim) | Subtitle / caption (verbatim) | Sound |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.5 | Hook: screen X from design-tool node 12:34 | zoom-in 110%, word-by-word appearance | "..." | "..." | whoosh |
| 2 | 2.5–6.0 | ... | ... | ... | ... | click |
| N | ... | End card: logo + CTA | ... | "..." | "..." | final accent |

## Rules (if they differ from the usual)
- Subtitles: word by word / by phrase, no periods, a black backing at 70%
- What not to do: <for example, do not change the background, do not show Free/Pro marks>

## How to fill it in
1. Voice-over and caption are written verbatim, exactly as they will sound and appear. "Here about search" is no good to the editor.
2. "On screen" names the source: a design-tool node id, a recording file, an icon id. A screen that is not in the sources must not be in the script.
3. Scene time is counted from words: words / 2.3 + 0.4 s. The sum equals the duration from the header.
4. The CTA in the header and in the last row match word for word. The end card goes right after the last line.
5. For 9:16 the script writes only what differs (another framing of a block); the video itself is assembled as a separate comp.
