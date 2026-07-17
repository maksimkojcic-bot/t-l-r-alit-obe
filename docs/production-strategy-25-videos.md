# Production Strategy - 25 Videos / Month

## Decision

The cheapest clean pipeline is **image-first + Remotion**, with optional short
Veo clips only when a scene needs real motion.

## Recommended pipeline

1. Generate reusable character and scene images with ChatGPT image generation.
2. Keep one strong image per scene or per episode.
3. Animate locally in Remotion:
   - camera push-ins;
   - punch zooms;
   - cuts and flashes;
   - subtitles;
   - voice timing;
   - simple audio-reactive elements.
4. Use ElevenLabs for voices.
5. Use Veo only for rare 4-8 second inserts.

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

Use Veo for at most 5-10 seconds per episode:

- 5 seconds at 720p Lite: about 0.25 USD per episode;
- 10 seconds at 720p Lite: about 0.50 USD per episode.

Then Remotion handles the rest locally.

## Quality target

The target look is:

- high-quality vertical 3D cartoon stills;
- aggressive reality-TV pacing;
- large readable subtitles;
- recurring fruit characters;
- motion created with camera moves, cuts, overlays, zooms, and audio rhythm.

This should be good enough for daily testing without burning video credits.
