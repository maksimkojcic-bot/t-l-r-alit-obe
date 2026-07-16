from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def load_env(path: Path | None = None) -> dict[str, str]:
    env_path = path or PROJECT_ROOT / ".env"
    values: dict[str, str] = {}
    if env_path.exists():
        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    merged = dict(os.environ)
    merged.update(values)
    return merged


def parse_time_range(value: str) -> tuple[float, float]:
    start_text, end_text = value.split("-", 1)
    return float(start_text), float(end_text)


def seconds_to_srt_time(seconds: float) -> str:
    milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def scene_text(scene: dict[str, Any]) -> str:
    return scene.get("text") or scene.get("dialogue") or scene.get("voiceover") or ""


def soften_subtitle(text: str) -> str:
    replacements = {
        "putain": "p*tain",
        "Putain": "P*tain",
        "merde": "m*rde",
        "Merde": "M*rde",
        "fait chier": "fait ch*er",
        "Fait chier": "Fait ch*er",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text


def split_subtitle(text: str, max_words_first_line: int = 7, max_words_total: int = 16) -> str:
    text = soften_subtitle(text.strip())
    words = text.split()
    if len(words) > max_words_total:
        head_count = max_words_first_line
        tail_count = max_words_total - head_count
        words = words[:head_count] + words[-tail_count:]
    if len(words) <= max_words_first_line:
        return " ".join(words)
    midpoint = min(max_words_first_line, max(1, len(words) // 2))
    return " ".join(words[:midpoint]) + "\n" + " ".join(words[midpoint:])
