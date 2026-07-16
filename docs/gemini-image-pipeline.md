# Gemini Image Pipeline

## Objectif

Generer une image verticale par scene a partir d'un episode JSON.

Le script principal est :

```bash
scripts/generate_scene_images.py
```

Par defaut, il ne consomme pas de credit : il ecrit seulement les prompts.

## Dry run

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/generate_scene_images.py episodes/episode-004.json --limit 2
```

## Generation reelle

Attention : `--run` appelle Gemini et peut consommer du budget Google AI.

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/generate_scene_images.py episodes/episode-004.json --limit 1 --run
```

## Modele

Modele recommande pour limiter le budget :

```text
gemini-3.1-flash-lite-image
```

Modele plus qualitatif, a utiliser plus rarement :

```text
gemini-3.1-flash-image
```

## Sources officielles

Google recommande les modeles Nano Banana pour la generation d'images. La documentation indique notamment `gemini-3.1-flash-lite-image`, `gemini-3.1-flash-image` et `gemini-3-pro-image`, et precise que les images generees incluent SynthID.
