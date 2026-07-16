from __future__ import annotations

import argparse
import csv
from pathlib import Path

from common import PROJECT_ROOT, load_json, scene_text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_json", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    episode = load_json(args.episode_json)
    characters = load_json(PROJECT_ROOT / "config" / "characters.json")
    output = args.output or args.episode_json.with_name(args.episode_json.stem + "-voices.csv")

    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["scene_id", "time", "speaker", "character_name", "voice_env", "text", "output_file"],
        )
        writer.writeheader()
        for scene in episode["scenes"]:
            speaker = scene.get("speaker", "host")
            character = characters.get(speaker, {})
            writer.writerow(
                {
                    "scene_id": scene["id"],
                    "time": scene["time"],
                    "speaker": speaker,
                    "character_name": character.get("name", speaker),
                    "voice_env": character.get("voice_env", ""),
                    "text": scene_text(scene),
                    "output_file": f"voices/{args.episode_json.stem}-{scene['id']}-{speaker}.mp3",
                }
            )

    print(output)


if __name__ == "__main__":
    main()
