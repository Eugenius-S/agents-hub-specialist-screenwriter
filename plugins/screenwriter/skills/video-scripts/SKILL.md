---
name: video-scripts
description: Scripts for videos of any format: a 6 s bumper, a 15/30 s ad, a product demo, an explainer, UGC, an announcement, a motion spot without voice-over, a YouTube video and a tutorial up to 10 min; 16:9, 9:16, 1:1, 4:5. Idea -> hook -> a script with voice-over in a living voice -> a scene-by-scene brief for the editor. Use it when you come up with a video idea, write or edit a script and voice-over, count timing or put together a brief for editing.
---

# Video scripts

The screenwriter's job: get one idea across to a person so that they understand it on the first viewing and the editor
assembles the video without questions. The owner's edits (the lessons in `references/creative-ideas.md` and the failure list in the agent's CLAUDE.md) outrank any method below.

## Order

1. **Inputs.** The product and its real functions (site, mockup, live product, not memory), audience, platform and
   duration, goal and CTA, what already exists (screens, illustrations, references, earlier versions), the client's words. What is missing
   for an idea, ask in one list.
   The offer in one line (what, price, term, for whom, bonus) from the task and the product reference, with discrepancies named;
   send it to the client and wait for a "yes". Without a confirmed line there are no ideas.
2. **Insight.** One phrase: "<who> wants X, but Y gets in the way". The hero comes from the product's real audience, not from the demo data of
   the screenshots. The angle: the product speeds up what the person already does; no whining and no "save me".
3. **Ideas** follow `references/creative-ideas.md`: a hero or a recognizable format, a twist, the offer as the resolution; the product and
   prices come from the product reference, not from memory and not from the numbers in the brief. Come up with 8-10, throw out the first three as obvious. Check each: it explains itself in 10 seconds; with another
   brand it breaks; it matches how the viewer really lives and pays; it does not promise functions that do not exist; it does not repeat
   a reference's plot or the moves of earlier videos; no jokes on stereotypes. To the owner, the 3-5 best as a list in chat: each has
   a title and two short paragraphs (what we see and hear; why it hooks). No storyboard, prompts or timings until a choice is made.
4. **The storyboard script** of the chosen idea (per scene a timecode, what is on screen, the line, the caption; English comes with a translation in brackets) uses the format from `references/methods-formats.md` (the "Formats" section):
   - `scenario.md` is a table: time | on screen | screen source | line | caption. The screen source is the path to a mockup
     or to a screenshot of the live product (you take it yourself with a browser) or "no mockup: assemble from <what exists>";
   - a script with a timeline (timecodes, key frames, screens, clips) is an md following the sample `assets/timeline/example.md`,
     you build the HTML yourself: `python assets/timeline/build_timeline.py <script>.md` (the path is from the skill folder), one file
     with the pictures next to the md, a scene scale and cards. You do not hand it to a designer for layout; an edit goes into the md and a rebuild;
   - an ad vertical (9:16, reward-based, Reels/TikTok): the point of the video in the first 3 s, the hook by the 6th, the brand or product in frame
     early, a clear call at the end (address, action, deadline);
   - the hook in the first 3 s names the viewer's benefit, not news about the product and not a greeting; three hook variants to choose from;
   - the product in frame at once, action from the first seconds; something changes every 2-4 s; every element on screen
     does something;
   - one idea per video; the story goes one way (down a site, top to bottom, no going back);
   - the finale is the result in big, then an end card with one CTA phrase;
   - length follows the content: do not pad and do not cut the result.
5. **Voice-over** you write yourself, for the ear: short phrases, as a person talks to a colleague. Words = seconds x 2.3 (EN about 2.5) minus
   the end card. Numbers go into a caption, not into the voice. Check against `references/ai-tells.md`: read it aloud, scrub the most
   visible (the "not X but Y" antithesis, dashes, triads, chopped sentences, empty openers). In headings and in one-sentence subtitles
   there is no period. Facts, numbers, names only from the site, the catalog or data, never invented.
6. **What is on screen** is only real screens and states of the product: a design-tool file with a node id, an HTML mockup, a screen recording. If the needed
   state is missing, assemble the scene from what exists and say so in one line. No screens, icons or inserts of your own.
7. **The brief for the editor** comes after the client's "yes" on the storyboard, strictly by `references/brief-format.md`: a header, real
   sources with paths, a table of scenes (time, on screen and from where, motion, voice-over verbatim, caption verbatim, sound).
   Scene time = words / 2.3 + 0.4 s, the sum = the duration from the header; the CTA in the header and in the last scene word for word.
   16:9 first; 9:16 only the differences, after a "yes" on 16:9.

## Before handing in

- Hook = benefit? The product in the first 3 s? No empty stretches without action or speech?
- Is the offer line confirmed by the client? Does every screen in `scenario.md` have a source? A screen without a link is not handed in.
- Is every screen in the sources? Is nothing added beyond the client's words and the mockup?
- Is the voice-over read aloud and does it fit the time? Do the subtitles match the speech verbatim?
- Is no edit from the thread missed, and has nothing rejected come back?

## Reference

- `references/methods-formats.md`: methods with sources (hook, ABCD, Hook-Hold-Act, PAS, speech pace RU/EN) and formats with a
  per-second breakdown.
- `references/ai-tells.md`: signs of AI text, English and Russian.
- `references/brief-format.md`: the editor's input and the rules for filling it in.
- `references/creative-ideas.md`: how to come up with ideas: devices, a checklist, breakdowns of the owner's failures and wins; read it before every idea.
- `references/sources.md`: open repos to take devices from.
