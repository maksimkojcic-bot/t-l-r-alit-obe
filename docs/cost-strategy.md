# Cost Strategy

## Decision

For now, do not use Gemini image generation as the default production path.

Reason: the current Gemini project returned a free-tier quota of `0` for
`gemini-3.1-flash-lite-image`. That means image generation is not currently
available for free on this API project.

## Recommended pipeline

1. Use ChatGPT image generation for core visual assets:
   - 5 anthropomorphic fruit contestants;
   - pineapple host;
   - broccoli coach;
   - villa gym;
   - kitchen;
   - bedroom;
   - confessional room.

2. Reuse those fruit reference assets instead of regenerating them every day.

3. Use Remotion to create the video:
   - camera zooms;
   - cuts;
   - shakes;
   - subtitles;
   - voice timing;
   - simple cartoon lip sync.

4. Use Google AI Studio only where it gives a clear advantage:
   - optional short video inserts;
   - rare special shots;
   - prompt experiments.

## Budget logic

Full AI video generation is expensive because it is billed by the second.
Image-based animation is much cheaper because the expensive part happens only
once, then Remotion animates locally.

## Rule

Never call a paid image or video generation endpoint automatically without an
explicit `--run` flag and a human decision.
