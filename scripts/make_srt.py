from __future__ import annotations

import argparse
from pathlib import Path

from common import load_json, parse_time_range, seconds_to_srt_time


def build_srt(episode: dict) -> str:
    blocks: list[str] = []
    for index, scene in enumerate(episode["scenes"], start=1):
        start, end = parse_time_range(scene["time"])
        text = scene.get("subtitle") or scene.get("text") or ""
        blocks.append(
            "\n".join(
                [
                    str(index),
                    f"{seconds_to_srt_time(start)} --> {seconds_to_srt_time(end)}",
                    text,
                ]
            )
        )
    return "\n\n".join(blocks) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_json", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    episode = load_json(args.episode_json)
    output = args.output or args.episode_json.with_suffix(".srt")
    output.write_text(build_srt(episode), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
