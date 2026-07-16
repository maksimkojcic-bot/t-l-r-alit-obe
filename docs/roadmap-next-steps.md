# Roadmap - Prochaines Etapes

## Phase 1 - Mettre le repo en place

Objectif : avoir une base GitHub propre.

- Importer le starter dans le repo `maksimkojcic-bot/t-l-r-alit-obe`.
- Ne jamais committer `.env`.
- Garder `.env.example` comme modele public.
- Faire un premier commit : `Initial automation structure`.

## Phase 2 - Verrouiller le concept

Objectif : eviter de changer de direction toutes les 48h.

- Valider le nom de travail : `Objectif 70` ou autre.
- Valider les 5 candidats recurrents.
- Valider l'animateur et le coach comme voix de production.
- Valider le ton : POV, humour oral/grossier, mauvais foi, sans body-shaming.
- Valider duree cible : 60 secondes.

## Phase 3 - Brancher les APIs

Objectif : verifier que les briques externes repondent.

- Ajouter `GEMINI_API_KEY` dans `.env`.
- Ajouter `ELEVENLABS_API_KEY` dans `.env`.
- Ajouter les 7 voix potentielles : host, coach, 5 candidats.
- Creer les scripts de verification Gemini et ElevenLabs.
- Activer un plafond de depense Google AI autour de 25-30 EUR.

## Phase 4 - Generateur d'episodes

Objectif : produire automatiquement des scripts originaux.

- Generer un episode JSON depuis un theme : balance, drive, sushi, donut, salle de sport.
- Generer les dialogues 60s avec structure POV.
- Generer les prompts images.
- Generer les sous-titres.
- Ajouter un score de securite : grossier OK, body-shaming non.

## Phase 5 - Voix et lip sync

Objectif : rendre les personnages vivants.

- Generer les MP3 ElevenLabs par scene.
- Produire un fichier de timings.
- Demarrer avec lip sync cartoon volume-based.
- Evoluer ensuite vers visemes/Rhubarb si besoin.

## Phase 6 - Montage Remotion

Objectif : exporter une vraie video verticale.

- Creer un projet Remotion.
- Lire l'episode JSON.
- Importer images + voix + sous-titres.
- Ajouter zooms, shakes, reactions, silences comiques.
- Exporter MP4 1080x1920.

## Phase 7 - Review et publication

Objectif : proteger la monetisation.

- Review manuelle avant publication.
- Verifier sous-titres, gros mots, contenu IA.
- Marquer le contenu comme IA quand la plateforme le demande.
- Publier d'abord en manuel, puis automatiser TikTok API plus tard.

## Priorite immediate

1. Pousser le starter sur GitHub.
2. Mettre la cle Gemini dans `.env`.
3. Choisir les voix ElevenLabs des 5 candidats.
4. Creer le premier script `generate_episode.py` pour Objectif 70.
5. Creer le premier test voix + sous-titres.
