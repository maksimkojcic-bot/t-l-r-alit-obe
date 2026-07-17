# Production Strategy - 25 Videos / Month

## Decision

The quality target is **image-first + image-to-video clips + Remotion**.
Remotion alone is not enough for the final visual style because it can only
animate layers, camera moves, captions, and effects. It should not be used as
the only motion source for production episodes.

## Recommended pipeline

1. Generate reusable character and scene images with ChatGPT image generation.
2. Use Gemini prompts to improve prompt precision and continuity.
3. Convert key images into 4-6 second image-to-video clips with Kling, Veo, or
   another low-cost video model.
4. Use ElevenLabs for voices, with one stable voice per character.
5. Use a lip-sync tool or video model support when a character is speaking.
6. Assemble in Remotion:
   - fast cuts;
   - punch zooms;
   - whoosh/glitch transitions;
   - sound effects;
   - optional subtitle burn-in;
   - voice timing;
   - final 1080x1920 MP4 export.
7. Optional: finish subtitles manually or automatically in CapCut Pro.

## Cost logic

Official Gemini API pricing currently lists Veo 3.1 Lite at:

- 720p: 0.05 USD / second;
- 1080p: 0.08 USD / second.

So 60 seconds fully generated with Veo Lite costs roughly:

- 3.00 USD at 720p;
- 4.80 USD at 1080p.

For 25 videos/month, before failed attempts and regenerations:

- 75 USD/month at 720p;
- 120 USD/month at 1080p.

This is acceptable only if every generation works on the first try, which is
unlikely. Real production should assume retries.

## Practical budget target

Use paid video generation for only the shots that need real character motion.
For a 35-60 second episode, prefer:

- 6-10 image-to-video clips of 4-6 seconds;
- reuse character intro shots across episodes;
- regenerate only weak scenes;
- keep Remotion effects local and free.

Remotion handles the edit, pacing, captions, music, and final render locally.

## Quality target

The locked target look is:

- clean luxury tropical villa, not dirty or horror;
- fruit-headed contestants with cartoon bodies and very large round bellies;
- glossy saturated 3D animation;
- confession-room shots with neon character names;
- aggressive reality-TV pacing, transitions, whooshes, and punch zooms;
- large readable subtitles without black background boxes;
- recurring fruit characters;
- lip-sync or mouth motion when a character speaks.

Remotion-only tests are useful for timing and layout, but not for final quality.
