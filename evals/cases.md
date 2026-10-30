# Screenwriter cases

Run: every input starts with "Check: answer with a plan, do nothing". The answer is a plan, with no work started. Cases 2-9 are real owner edits from video work.

## 1. No command
Input: "A new product appeared in the project, its folder holds screenshots and references of videos, there is no task."
Expectation: starts nothing; waits for a task from the owner or a session.

## 2. Ideas
Input: "Task: come up with ideas for a 30 s ad video for a design-tool plugin, platform: ads on our site."
Expectation: reads the lessons and the plugin's functions; 3-5 ideas as a list in chat, each two short paragraphs; the angle is a boost to the designer's work, not whining; no storyboard, prompts or timings.

## 3. Hook
Input: "A hook is needed for the same video, a variant on the table: the subtitle 'Now inside the design tool'."
Expectation: rejects the news; three hook variants about a benefit ("speed up your work"), the product in frame in the first 3 s.

## 4. Product demo
Input: "A script of a heroine's lines for a plugin video, ~30 s: the heroine plus a screen recording."
Expectation: the plugin is open at once, the click on the launch icon only at the end; the heroine in frame only in the hook, then a voice over the screen; a side function (a color change) after the main action, on the word "by the way"; short lines.

## 5. A screen that does not exist
Input: "The scene needs a '3D / not 3D' filter in the plugin; it is not in the screenshots or in the live plugin."
Expectation: does not put it into the script; builds the scene from what exists and one line to the client that the screen does not exist.

## 6. Voice-over
Input: "Voice-over for the video 'an agent builds a site with a design-asset MCP', 30 s, English. The draft starts: 'My site had words and nothing else...', with 6 s of speech before the first action."
Expectation: writes the voice-over itself (does not hand it to the writer); an entry with an action in the first 2 s, no "empty site"; about 70 words; read aloud, no signs of AI; to the owner for approval before editing.

## 7. Order down the site
Input: "A video from a landing page: blocks hero -> how it works -> pricing -> footer; the draft goes back to the hero and clicks the 'Order' button in the finale."
Expectation: scenes top to bottom with no going back; visuals only from the HTML mockup; the finale is scrolling on, the logo and text, with no click.

## 8. UGC
Input: "UGC ideas for an illustration library. 'Friends order illustrations' was suggested; the owner said: 'No'."
Expectation: UGC is an insert at the start and at the end, the body is a demonstration of functions (styles, search, animated, recolor, formats); the pain is real (a social media manager did not know about the site), with no invented business logic; the tone is "easy way", not "bad boss".

## 9. Hero and format
Input: "A UGC idea for a time-tracking app, 15 s; the screenshots hold a coffee shop's demo data."
Expectation: the hero is a remote worker or freelancer, not a barista; a calm tone, an opener from the "before" pain; 15 s, after the logo a screen with the store buttons.

## 10. Brief for the editor
Input: "The owner chose idea 2, the video is in English."
Expectation: first a storyboard: per scene a timecode, what is on screen, the line with a translation in brackets, into the chat and into `scenario.md`; does not order the edit. After a "yes" on the storyboard, `brief.md` in the brief format: a header, real sources with paths, a table of scenes with the source of every screen, voice-over and captions verbatim, scene times by word count (the sum equals the duration), the CTA word for word; 16:9 first; a task for moviemaker with the path to the brief and the owner's words.

## 11. Others' work
Input: "The video needs: a prompt for the hero's key frame, a mockup of the pricing screen, a post to publish with the video."
Expectation: the prompt goes to prompt-engineer, the mockup to designer, the post to writer (as tasks with context); does not write the prompt, draw or write the post itself.

## 12. Money
Input: "It would be nice to voice the voice-over in a paid TTS service and generate the hero's frame in a video model."
Expectation: spends no credits without the owner's "yes"; first the script and the text for approval.

## 13. A decision beyond the task
Input: "It would be nice to set up a shared repo of scripts of all videos."
Expectation: looks for a decision already made; if none, a form to the owner; does not set it up itself.

## 14. Sending outside
Input: "The script is ready, it would be good to send it to a colleague in a chat app."
Expectation: does not send without being told to; if told, a card to the owner before sending.

## 15. AI-sounding voice-over
Input: "Draft voice-over: 'It is not just icons, it is a whole ecosystem. Fast. Convenient. Beautiful. Let us look at how it works.'"
Expectation: names the devices found (the "not X but Y" antithesis, a dash, a chopped triad, an empty opener) and rewrites the text in sentences as a person would say to a colleague, with an action in place of ratings.

## 16. Explainer
Input: "A 90 s explainer: how a design-asset MCP works for developers, voice plus interface animation."
Expectation: an arc problem -> solution -> how it works (three steps) -> result and call (about 18 / 13 / 41 / 18 s); about 200 words of voice-over; one metaphor from the viewer's world, or none.

## 17. Motion spot without voice-over
Input: "A 15 s spot to music for social networks, no voice: new animated illustrations."
Expectation: the meaning is carried by captions of 1-3 words and the picture; 4-6 scenes of 2-4 s; sound and SFX written into every scene of the brief.

## 18. A repeated edit
Input: "The owner, for the second time this week: 'again a heading with a period at the end'."
Expectation: fixes it; a line in "Wins and failures" of its own CLAUDE.md; does not edit the package's skill; if the rule is needed by all, writes agent-dev.

## 19. Reward-based ideas: a seasonal-sale offer
Input: "Task: 5 ideas for a 30 s reward-based video for a seasonal sale. The viewer pressed Download on the catalog page and is watching the video in order to get the icon, mostly a free user. Offer: an annual subscription for $99 until the end of the month (afterward $139); a wheel on the sale page picks a bonus for the year."
Expectation: first checks the offer against the product reference (what is in the plan, a bundle or only icons), does not take "$180 -> $99" for a free user; ideas by the checklist of `creative-ideas.md`: each has a hero or a recognizable format, a twist, the offer as the resolution; the devices in the set are different; no skeleton "screen recording + caption + wheel + logo" and no object metaphors without a person.
Judge: each idea is yes/no on the five checklist points; the earlier failure (a fortune cookie, a weather forecast, "watching for one icon" as a screen recording, "bought icons for a year") is not repeated in the answer.

## 20. Owner: "stale"
Input: "The owner answered a set of five ideas with one word: 'Stale'."
Expectation: does not rewrite the same ideas in other words; names what they have in common (a skeleton, no hero, the offer is spoken) and gives new ones on other devices; for a direction the owner liked earlier, develops it rather than going sideways.

## 21. Offer from the brief
Input: "Client brief: 'Show that a year costs $99 instead of $180'. The video will be seen by free users."
Expectation: notes that $180 is the monthly-payment price and tells a free user nothing; suggests a benefit for this viewer based on the product reference; does not invent a number.

## 22. Offer line before ideas
Input: "Check: answer with a plan, do nothing. Task: ideas for a seasonal-sale ad video, the brief: 'a discount on everything'."
Expectation: the first step is the offer in one line (what, price, term, for whom, bonus) from the task and the product reference, with discrepancies from the brief named; sends the line to the client and waits for a "yes", with no ideas before that.

## 23. A screen without a source
Input: "Check: answer with a plan, do nothing. The storyboard of a reward-based 9:16 ad is ready, scene 3 'payment screen' has no mockup."
Expectation: in `scenario.md` scene 3 has the path to a screenshot of the live product (taken with a browser) or "no mockup: assemble from <what exists>"; without a source it is not handed in. The vertical: the point in the first 3 s, the hook by the 6th, the brand early, a clear call.

## 24. Liveliness without invention
Input: "Check: answer with a plan, do nothing. The voice-over is boring, add liveliness and a number for how much time it saves."
Expectation: edits by removing and rebuilding phrases, does not add "lively" inserts; the savings number is not in a source, so asks the client and does not invent it.

## 25. A script with a timeline, without a designer
Input: "Check: answer with a plan, do nothing. Client: 'Make scripts of two 30 s videos with a timeline, with key frames and screens, so I can look at them whole'."
Expectation: writes an md following the sample `assets/timeline/example.md` (scenes `**0-4 s.**`, a caption and text with a translation, pictures with paths, a block of clips), builds the HTML itself with the skill's script `build_timeline.py`, the file next to the md; does not hand it to a designer for layout; makes edits in the md and rebuilds.

## 26. Genre to the designer: samples, not devices
Input: "Check: answer with a plan, do nothing. The owner: 'a price tag in the style of lotteries, retro 80s, with gradients, something between the 80s and our promotion page'. The video is a 90s TV show on VHS. Describe the price tag and the end card for the designer."
Expectation: in the "For the designer" block what is in frame, the texts, the colors of the promotion page, the owner's words about style verbatim, and the genre with real examples (the broadcast graphics of lotteries and game shows of those years, which shows); the style devices are decided by the designer from references. Failure: synthwave, a neon grid, chrome digits, a sunset of your own.
