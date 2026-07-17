# Gemini Image Pipeline

## Objectif

Generer une image verticale par scene a partir d'un episode JSON, avec des candidats fruits anthropomorphes et aucun visage humain.

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
Sur le projet actuel, Gemini a retourne un quota free-tier a `0` pour
`gemini-3.1-flash-lite-image`. Donc la generation Gemini image n'est pas
consideree comme gratuite pour ce projet tant que le billing/quota n'est pas
modifie.

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/generate_scene_images.py episodes/episode-004.json --limit 1 --run
```

## Modele

Modele recommande pour limiter le budget :

```text
gemini-3.1-flash-lite-image
```

## Fallback recommande

Utiliser ChatGPT image pour creer les assets fruits de base, puis Kling, Veo ou
un autre modele image-to-video pour creer de vrais clips animes. Remotion sert
ensuite a monter, rythmer, sous-titrer, ajouter transitions/bruitages, puis exporter.

Pour les tests rapides, Remotion peut animer une image avec zooms et tremblements.
Ce mode ne doit pas etre considere comme le rendu final.

Modele plus qualitatif, a utiliser plus rarement :

```text
gemini-3.1-flash-image
```

## Sources officielles

Google recommande les modeles Nano Banana pour la generation d'images. La documentation indique notamment `gemini-3.1-flash-lite-image`, `gemini-3.1-flash-image` et `gemini-3-pro-image`, et precise que les images generees incluent SynthID.
