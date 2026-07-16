from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from common import load_json, scene_text


BLOCKED_PATTERNS = [
    r"\bgros porc\b",
    r"\bgrosse vache\b",
    r"\bbaleine\b",
    r"\bmonstre\b",
    r"\bdegoutant(?:e|s)?\b",
    r"\bobese de merde\b",
    r"\bgras(?:se)? comme\b",
    r"\btu merites pas\b",
]

WARNING_PATTERNS = [
    r"\bmaigrir vite\b",
    r"\bperdre \d+\s?kg en\b",
    r"\bregime miracle\b",
    r"\bne mange plus\b",
    r"\bsaute les repas\b",
]


def scan_text(text: str, patterns: list[str]) -> list[str]:
    found: list[str] = []
    lowered = text.lower()
    for pattern in patterns:
        if re.search(pattern, lowered):
            found.append(pattern)
    return found


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_json", type=Path)
    args = parser.parse_args()

    episode = load_json(args.episode_json)
    failures: list[str] = []
    warnings: list[str] = []
    for scene in episode.get("scenes", []):
        text = " ".join(
            [
                scene_text(scene),
                scene.get("subtitle", ""),
                scene.get("visual_prompt", ""),
            ]
        )
        blocked = scan_text(text, BLOCKED_PATTERNS)
        warning = scan_text(text, WARNING_PATTERNS)
        if blocked:
            failures.append(f"{scene.get('id')}: blocked={blocked}")
        if warning:
            warnings.append(f"{scene.get('id')}: warning={warning}")

    for item in warnings:
        print("WARNING", item)
    for item in failures:
        print("FAILED", item)

    if failures:
        sys.exit(1)
    print("content_safety_check: OK")


if __name__ == "__main__":
    main()
