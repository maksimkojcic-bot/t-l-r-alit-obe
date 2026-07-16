# GitHub Setup

Repo cible :

https://github.com/maksimkojcic-bot/t-l-r-alit-obe

## Etat actuel

Le depot est public et vide.

## Option simple : GitHub Desktop

1. Installe GitHub Desktop.
2. Connecte ton compte GitHub.
3. Clone le repo `maksimkojcic-bot/t-l-r-alit-obe`.
4. Copie les fichiers de ce starter dans le dossier clone.
5. Clique **Commit to main**.
6. Clique **Push origin**.

## Option terminal

Quand `git` est disponible sur ton Mac :

```bash
cd /Users/loupwallstreet/Documents/Codex/2026-07-06/salut-je-voulais-que-tu-m/outputs/t-l-r-alit-obe
git init
git branch -M main
git add .
git commit -m "Initial automation structure"
git remote add origin https://github.com/maksimkojcic-bot/t-l-r-alit-obe.git
git push -u origin main
```

Si macOS demande les Command Line Tools, installe-les ou utilise GitHub Desktop.

## Important

Ne jamais committer `.env`. Le fichier `.gitignore` l'exclut deja.
