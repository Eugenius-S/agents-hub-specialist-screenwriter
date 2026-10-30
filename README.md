# The Screenwriter specialist for agents-hub

A permanent hub agent: comes up with ideas and scripts for videos of any format (ads, product demos, explainers, UGC, announcements, motion spots), writes voice-over in a living voice and hands the editor a scene-by-scene brief.

- Starts only on a task from the owner or another session.
- Ideas as a list of two paragraphs each, the script after a choice, the brief for the editor after a "yes" on the script.
- In frame only real product screens; voice-over without signs of AI text, timing by word count.
- Editing, prompts, mockups, animation and the texts around the video go to specialists; paid voice-over and generation only with the owner's "yes".

Installed through the hub's specialist catalog. The tools in `hub-plugin.json` -> `agent.tools.optional` are issued by the hub if they are in its catalog. The `video-scripts` skill holds the method, formats with timings, signs of AI text, the brief format for the editor and lessons learned. Check after installing: the cases in `evals/cases.md`.
