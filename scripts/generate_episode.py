from __future__ import annotations

import argparse
import random
from pathlib import Path
from typing import Any

from common import PROJECT_ROOT, load_json, save_json, split_subtitle


THEMES: dict[str, dict[str, Any]] = {
    "balance": {
        "title": "La Balance Chelou",
        "pov": "POV : la balance s'est levee ce matin pour insulter l'ambiance.",
        "situation": "digital scale glowing in a luxury reality TV villa bathroom",
        "speaker": "candidate_2",
        "line_1": "Chef, elle a bugue cette merde. J'ai pose un pied, elle a appele les secours.",
        "line_2": "Deja hier j'ai pas mange. J'ai juste mis le donut en garde a vue dans ma bouche.",
        "authority": "Arrete tes conneries. La balance t'agresse pas, elle lit juste le dossier.",
        "group": "Une balance qui parle comme ca, faut la sortir de la villa avant qu'elle prenne la confiance.",
        "cliff": "Mais quand le coach est monte dessus, elle a affiche : surcharge d'excuses detectee.",
    },
    "donut": {
        "title": "Le Donut du Reveil",
        "pov": "POV : la production pose un donut a cote de ton lit comme une menace.",
        "situation": "shiny donut on a bedside table with a warning card",
        "speaker": "candidate_2",
        "line_1": "Frere je l'ai pas mange, je l'ai interroge avec ma bouche. Nuance.",
        "line_2": "Le donut me regardait mal. A un moment faut se defendre, merde.",
        "authority": "Pose ce donut lentement. On negocie pas avec un cercle glace qui manipule les faibles.",
        "group": "Moi je dis le donut il a provoque. Il etait trop brillant, cette saloperie savait ce qu'elle faisait.",
        "cliff": "La camera de nuit montre une main qui revient chercher les vermicelles.",
    },
    "sushi": {
        "title": "L'Atelier Sushi",
        "pov": "POV : atelier sushi, mais tout le monde finit au tribunal du riz.",
        "situation": "reality show kitchen with sushi plates under dramatic spotlights",
        "speaker": "candidate_1",
        "line_1": "Chef, moi je roule pas un sushi, je roule une strategie. Respecte le projet.",
        "line_2": "Le riz colle a mes doigts, donc techniquement c'est lui qui cherche les problemes.",
        "authority": "Personne ne panique. Le wasabi sent la peur et vous sentez deja la defaite.",
        "group": "J'ai vu quelqu'un cacher une sauce dans sa chaussette. On est dans une villa ou dans un braquage ?",
        "cliff": "Au moment du vote, un maki disparait devant tout le monde.",
    },
    "drive": {
        "title": "Le Drive de la Villa",
        "pov": "POV : la production ouvre un drive dans le jardin pour foutre le chaos.",
        "situation": "fake fast-food drive window built inside a tropical villa garden",
        "speaker": "candidate_5",
        "line_1": "Chef, si je commande pour la table, les calories sont collectives. C'est des maths.",
        "line_2": "J'ai dit menu enfant, donc c'est pas grave, c'est educatif cette connerie.",
        "authority": "Recule du micro. La sauce t'a deja reconnu, arrete de faire le discret.",
        "group": "Il a demande sans oignon pour faire croire qu'il controle la situation. Frere t'as pris trois sauces.",
        "cliff": "Le ticket sort avec une commande que personne n'assume.",
    },
    "salle_sport": {
        "title": "La Salle de Sport",
        "pov": "POV : premiere seance de sport, le tapis a declare la guerre.",
        "situation": "tiny villa gym, treadmill, dumbbells, dramatic reality TV camera",
        "speaker": "candidate_4",
        "line_1": "Putain le tapis avance tout seul, deja cette machine a une attitude de merde.",
        "line_2": "Moi je cours pas, je negocie avec mes genoux. Ils sont syndiques.",
        "authority": "Respire. Le tapis t'en veut pas personnellement, mais il te respecte pas non plus.",
        "group": "Il a mis pause au bout de huit secondes et il a appele ca une serie. Chef, c'etait une bande-annonce.",
        "group_subtitle": "Pause au bout de huit secondes.\nChef, c'etait une bande-annonce.",
        "cliff": "Le coach annonce que l'echauffement n'avait meme pas commence.",
    },
    "frigo": {
        "title": "Le Frigo Interdit",
        "pov": "POV : le frigo de la villa est sous surveillance parce que tout le monde ment.",
        "situation": "luxury villa fridge with red laser beams and security camera",
        "speaker": "candidate_3",
        "line_1": "J'ai pas ouvert le frigo, j'ai verifie s'il respirait encore. C'est citoyen.",
        "line_2": "La lumiere s'est allumee toute seule, moi je suis victime de cette armoire froide.",
        "authority": "Eloigne-toi du fromage. Il te manipule depuis trois minutes et tu fais semblant de rien.",
        "group": "Depuis quand un yaourt a besoin d'un garde du corps ? Ce frigo prepare un coup d'Etat.",
        "cliff": "Le frigo bippe et affiche : tentative de seduction detectee.",
    },
}


SCENE_TIMES = ["0-3", "3-10", "10-24", "24-39", "39-51", "51-60"]


def scene(
    scene_id: str,
    time: str,
    speaker: str,
    text: str,
    visual_prompt: str,
    scene_type: str,
    subtitle: str | None = None,
) -> dict[str, str]:
    return {
        "id": scene_id,
        "time": time,
        "type": scene_type,
        "speaker": speaker,
        "text": text,
        "subtitle": subtitle or split_subtitle(text),
        "visual_prompt": visual_prompt,
    }


def build_episode(episode_number: int, theme_name: str, seed: int | None = None) -> dict[str, Any]:
    if seed is not None:
        random.seed(seed)
    series = load_json(PROJECT_ROOT / "config" / "series.json")
    characters = load_json(PROJECT_ROOT / "config" / "characters.json")
    theme = THEMES[theme_name]
    base_style = series["visual_style_prompt"]

    group_speaker = random.choice(["candidate_1", "candidate_3", "candidate_4", "candidate_5"])

    return {
        "series": series["working_title"],
        "episode_number": episode_number,
        "title": theme["title"],
        "theme": theme_name,
        "duration_seconds_target": series["format"]["duration_seconds_target"],
        "format": series["format"],
        "prize": series["prize"],
        "aigc": True,
        "style": "POV sketch, aggressive French oral humor, frequent casual profanity, no body-shaming",
        "scenes": [
            scene(
                "s01_pov",
                SCENE_TIMES[0],
                "host",
                theme["pov"],
                f"{base_style} Opening POV title card, {theme['situation']}, fast TikTok hook.",
                "pov_hook",
            ),
            scene(
                "s02_situation",
                SCENE_TIMES[1],
                theme["speaker"],
                theme["line_1"],
                f"{base_style} {characters[theme['speaker']]['prompt']}. Scene: {theme['situation']}. Close-up reaction.",
                "situation",
            ),
            scene(
                "s03_excuse",
                SCENE_TIMES[2],
                theme["speaker"],
                theme["line_2"],
                f"{base_style} Confessional interview room, exaggerated serious explanation, funny guilty expression.",
                "excuse",
            ),
            scene(
                "s04_authority",
                SCENE_TIMES[3],
                "coach",
                theme["authority"],
                f"{base_style} {characters['coach']['prompt']}. Coach entering like a detective, absurd authority.",
                "authority",
            ),
            scene(
                "s05_group_reaction",
                SCENE_TIMES[4],
                group_speaker,
                theme["group"],
                f"{base_style} Five contestants in a villa group scene, dramatic reality TV reaction, comedic tribunal framing.",
                "group_reaction",
                theme.get("group_subtitle"),
            ),
            scene(
                "s06_cliffhanger",
                SCENE_TIMES[5],
                "host",
                theme["cliff"],
                f"{base_style} Suspenseful close-up, absurd clue revealed, everyone freezes, cliffhanger ending.",
                "cliffhanger",
            ),
        ],
        "caption": f"{theme['title']} dans Objectif 70. Qui va craquer pour les 100 000 EUR ? #Objectif70 #Humour #Telerealite #IA #TikTokFrance",
        "publishing_notes": {
            "manual_review_required": True,
            "mark_as_ai_generated": True,
            "do_not_copy_reference_creator": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episode", type=int, required=True)
    parser.add_argument("--theme", choices=sorted(THEMES), default="balance")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--list-themes", action="store_true")
    args = parser.parse_args()

    if args.list_themes:
        for theme in sorted(THEMES):
            print(theme)
        return

    episode = build_episode(args.episode, args.theme, args.seed)
    output_path = PROJECT_ROOT / "episodes" / f"episode-{args.episode:03}.json"
    save_json(output_path, episode)
    print(output_path)


if __name__ == "__main__":
    main()
