from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

from common import PROJECT_ROOT, load_env


def synthesize(api_key: str, model_id: str, voice_id: str, text: str, output_path: Path) -> None:
    payload = {
        "text": text,
        "model_id": model_id,
        "voice_settings": {
            "stability": 0.48,
            "similarity_boost": 0.82,
            "style": 0.38,
            "use_speaker_boost": True,
        },
    }
    request = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(request, timeout=120) as response:
        output_path.write_bytes(response.read())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("voice_plan_csv", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--fallback-voice-env",
        help="Use this .env voice id when a scene voice is missing. Useful for pipeline tests.",
    )
    args = parser.parse_args()

    env = load_env()
    api_key = env.get("ELEVENLABS_API_KEY", "")
    model_id = env.get("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")
    if not api_key and not args.dry_run:
        sys.exit("Missing ELEVENLABS_API_KEY in .env")

    with args.voice_plan_csv.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            voice_id = env.get(row["voice_env"], "")
            fallback_voice_id = env.get(args.fallback_voice_env or "", "")
            if not voice_id and fallback_voice_id:
                voice_id = fallback_voice_id
            output_path = PROJECT_ROOT / row["output_file"]
            if args.dry_run:
                state = "OK" if voice_id else f"MISSING {row['voice_env']}"
                if fallback_voice_id and row["voice_env"] != args.fallback_voice_env:
                    state += f" fallback={args.fallback_voice_env}"
                print(f"{state}: {row['character_name']} -> {output_path}")
                continue
            if not voice_id:
                sys.exit(f"Missing {row['voice_env']} in .env")
            try:
                synthesize(api_key, model_id, voice_id, row["text"], output_path)
                print(output_path)
            except urllib.error.HTTPError as error:
                detail = error.read().decode("utf-8", errors="replace")
                sys.exit(f"ElevenLabs error {error.code}: {detail}")


if __name__ == "__main__":
    main()
