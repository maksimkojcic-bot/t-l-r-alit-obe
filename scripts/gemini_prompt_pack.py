from __future__ import annotations

import argparse
from pathlib import Path

from common import load_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_json", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    episode = load_json(args.episode_json)
    output = args.output or args.episode_json.with_name(args.episode_json.stem + "-prompts.md")
    lines = [
        f"# {episode['series']} - Episode {episode['episode_number']:03}",
        "",
        f"## {episode['title']}",
        "",
        "Use these prompts for Gemini image generation. Keep character designs consistent across scenes.",
        "",
    ]
    for scene in episode["scenes"]:
        lines.extend(
            [
                f"## {scene['id']} ({scene['time']})",
                "",
                "Prompt:",
                "",
                scene["visual_prompt"],
                "",
                "Subtitle:",
                "",
                scene.get("subtitle", ""),
                "",
            ]
        )
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
