# Objectif 70 - Automation TikTok / Shorts

Starter de production pour une mini telerealite 3D cartoon verticale avec des candidats fruits anthropomorphes.

## Concept

Des fruits anthropomorphes participent a une competition de transformation pour passer sous la barre symbolique des **70 kg** et gagner **100 000 EUR**. Chaque episode met en scene une tentation absurde, un conflit de villa, une epreuve ou une decision de groupe.

Le ton vise : humour POV tres oral, agressif, telerealite exageree, personnages attachants, montage rapide, sous-titres lisibles, langage familier/grossier maitrise.

Le ton evite : humiliation du corps humain, insultes sur le poids de vraies personnes, blagues degradantes sur des humains, medicalisation lourde, copie directe d'un createur existant.

## Structure

```text
assets/
  images/
  videos/
  music/
  sound_fx/
config/
  characters.json
  series.json
docs/
  automation-plan.md
  concept-bible.md
  content-safety.md
  github-setup.md
episodes/
prompts/
scripts/
voices/
renders/
```

## APIs

Les secrets vont dans `.env`, jamais dans le README.

Copie `.env.example` vers `.env`, puis remplis les valeurs :

```bash
cp .env.example .env
```

## Pipeline cible

1. Generer un script d'episode.
2. Generer les prompts visuels Gemini.
3. Generer les voix ElevenLabs.
4. Creer sous-titres + timings.
5. Monter dans Remotion.
6. Exporter MP4 vertical.
7. Review manuelle.
8. Publication TikTok / YouTube Shorts.

## Commandes utiles

Utilise le Python fourni par Codex si `python3` macOS demande Xcode :

```bash
cd /Users/loupwallstreet/Documents/Codex/2026-07-06/salut-je-voulais-que-tu-m/outputs/t-l-r-alit-obe
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_episode_assets.py --episode 3 --theme donut
```

Themes disponibles :

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/generate_episode.py --episode 3 --list-themes
```

Verifier la config sans afficher les cles :

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_config.py
```

Verifier ElevenLabs :

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_elevenlabs.py
```

Generer les prompts images sans consommer de credits :

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/generate_scene_images.py episodes/episode-004.json --limit 2
```

Generer une image reelle avec Gemini :

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/generate_scene_images.py episodes/episode-004.json --limit 1 --run
```

Note cout : sur le projet actuel, Gemini image a retourne un quota gratuit a
`0`. La strategie recommandee est donc de creer les assets fruits avec
ChatGPT image, puis de monter/animer avec Remotion.

Generer les voix apres validation :

```bash
/Users/loupwallstreet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/elevenlabs_tts.py episodes/episode-003-voices.csv --dry-run
```

## Format valide apres analyse

- Duree cible : environ 60 secondes.
- 5 candidats recurrents sous forme de fruits, avec animateur/coach fruits en voix de production si besoin.
- Structure POV / sketch simple / chute forte.
- Langage : francais oral, direct, parfois grossier, mais sans attaque sur le corps.
- Humour : mauvaise foi agressive, panique, contraste, autorite absurde, tentation alimentaire, clashs rapides.

## Premiere decision creative

Nom de travail recommande : **Objectif 70**.

Pourquoi : le nom annonce l'objectif sans reduire les candidats a leur poids. C'est plus propre pour les plateformes et plus durable pour faire une serie humoristique.
