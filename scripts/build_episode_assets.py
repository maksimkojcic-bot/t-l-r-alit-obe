from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from common import PROJECT_ROOT


PYTHON = sys.executable


def run(command: list[str]) -> None:
    print("+ " + " ".join(command))
    subprocess.run(command, cwd=PROJECT_ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episode", type=int, required=True)
    parser.add_argument("--theme", required=True)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    generate_command = [PYTHON, "scripts/generate_episode.py", "--episode", str(args.episode), "--theme", args.theme]
    if args.seed is not None:
        generate_command.extend(["--seed", str(args.seed)])
    run(generate_command)

    episode_path = Path("episodes") / f"episode-{args.episode:03}.json"
    run([PYTHON, "scripts/content_safety_check.py", str(episode_path)])
    run([PYTHON, "scripts/make_srt.py", str(episode_path)])
    run([PYTHON, "scripts/voice_plan.py", str(episode_path)])
    run([PYTHON, "scripts/gemini_prompt_pack.py", str(episode_path)])


if __name__ == "__main__":
    main()
