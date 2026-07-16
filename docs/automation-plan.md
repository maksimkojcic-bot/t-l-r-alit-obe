# Automation Plan

## Objectif

Produire une video verticale par jour avec validation manuelle avant publication.

## Briques

### 1. Script

Entree :

- theme du jour ;
- personnages presents ;
- type de tentation ;
- duree cible.

Sortie :

- JSON episode ;
- dialogues ;
- prompts visuels ;
- sous-titres.

### 2. Images / decors

Google AI Studio / Gemini sert a generer :

- personnages ;
- decors ;
- props : donuts, sushi, balance, plateau, cuisine, villa ;
- plans fixes ou courtes variations.

Priorite budget : images plutot que video longue.

### 3. Voix

ElevenLabs genere :

- animateur ;
- coach ;
- 4 candidats.

Chaque scene produit un MP3 et un fichier de timing.

### 4. Lip sync

Approche recommandee :

- lip sync cartoon dans Remotion ;
- bouche ouverte/fermee selon volume audio au debut ;
- ensuite visemes avec Rhubarb Lip Sync ou timings ElevenLabs.

### 5. Montage

Remotion :

- scenes sequentielles ;
- zooms et shakes drama ;
- sous-titres ;
- bruitages ;
- musique ;
- export MP4 1080x1920.

### 6. Publication

TikTok API officielle :

- OAuth ;
- upload video ;
- `is_aigc: true` ;
- publication en prive au debut si l'app n'est pas auditee.

## Budget

Pour rester sous 30 EUR / mois cote Google :

- limiter la generation video IA ;
- utiliser surtout images + montage Remotion ;
- reutiliser personnages et decors ;
- generer 6 a 10 images par episode maximum ;
- activer un spend cap Google AI.

La video IA longue peut faire exploser le budget. Elle doit rester exceptionnelle.
