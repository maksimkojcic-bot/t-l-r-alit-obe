# Project Memory

Last updated: 2026-07-17

## Project

The project is a TikTok/Shorts automation pipeline for a fictional AI reality show:

- working names: `Objectif 70`, `Fruit Shore`;
- vertical videos for TikTok, about 35-60 seconds;
- recurring fruit characters competing in a reality show format;
- goal in the story: go under 70 kg / win 100 000 euros;
- tone: edgy, vulgar enough for viral TikTok, but aimed at fictional fruit characters and absurd situations, not real people.

## Locked User Preferences

- The user wants anthropomorphic fruit characters instead of human faces.
- The user wants very large round cartoon bellies, clearly exaggerated.
- The style should be clean, glossy, colorful, luxury villa reality TV.
- Do not make the characters dirty, grimy, horror, or gloomy.
- The reference style is the user's CapCut video `0605(4).mov`.
- The user does not want a final video that is just one still image shaking.
- The final video needs real movement, scene changes, transitions, sound effects, and pacing.
- The user wants lip-sync or at least visible mouth movement when characters talk.
- Subtitles should be white bold text with black stroke only, without a black background rectangle.
- CapCut Pro can be used for final auto-captions if needed.
- The user prefers validating the exact visual style before spending credits on paid video APIs.

## Tooling Direction

- ChatGPT / image generation: create strong character and scene images.
- Gemini / Google AI: improve prompts, continuity, and shot planning; possibly generate assets if cost/quota is acceptable.
- Kling, Veo, or a similar image-to-video model: create real animated clips from still images.
- ElevenLabs: character voices, one stable voice per character.
- Lip-sync tool: mouth movement if the video model does not handle it.
- Remotion: final assembly, timing, transitions, sound effects, music, optional subtitles, MP4 export.
- CapCut Pro: optional final subtitle/effects polish.

## Current GitHub Local Repo

```text
/Users/loupwallstreet/Documents/t-l-r-alit-obe tele auto
```

Remote:

```text
https://github.com/maksimkojcic-bot/t-l-r-alit-obe.git
```

Terminal push may fail because GitHub authentication is handled by GitHub Desktop. If it fails, tell the user to click `Push origin` in GitHub Desktop.

## Sensitive Data

Never store API keys or tokens in this memory file, Git commits, prompts, or docs. Keep secrets only in `.env` or the user's secure account settings.
