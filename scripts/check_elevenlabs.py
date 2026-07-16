from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from pathlib import Path

from common import PROJECT_ROOT, load_env


VOICE_KEYS = [
    "VOICE_HOST",
    "VOICE_COACH",
    "VOICE_CANDIDATE_1",
    "VOICE_CANDIDATE_2",
    "VOICE_CANDIDATE_3",
    "VOICE_CANDIDATE_4",
    "VOICE_CANDIDATE_5",
]


def request_json(path: str, api_key: str) -> tuple[int, dict]:
    request = urllib.request.Request(
        f"https://api.elevenlabs.io/v1{path}",
        headers={"xi-api-key": api_key, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            text = response.read().decode("utf-8", errors="replace")
            return response.status, json.loads(text) if text else {}
    except urllib.error.HTTPError as error:
        text = error.read().decode("utf-8", errors="replace")
        try:
            body = json.loads(text)
        except json.JSONDecodeError:
            body = {"raw": text[:500]}
        return error.code, body


def request_tts(api_key: str, model_id: str, voice_id: str, text: str, output_path: Path) -> tuple[int, dict | None]:
    payload = json.dumps({"text": text, "model_id": model_id}).encode("utf-8")
    request = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        data=payload,
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(response.read())
            return response.status, None
    except urllib.error.HTTPError as error:
        text = error.read().decode("utf-8", errors="replace")
        try:
            body = json.loads(text)
        except json.JSONDecodeError:
            body = {"raw": text[:500]}
        return error.code, body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-tts", action="store_true", help="Generate tiny MP3 samples. This consumes characters.")
    args = parser.parse_args()

    env = load_env()
    api_key = env.get("ELEVENLABS_API_KEY", "")
    model_id = env.get("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")
    print(f"ELEVENLABS_API_KEY: {'set len=' + str(len(api_key)) if api_key else 'missing'}")
    if not api_key:
        return

    status, body = request_json("/voices", api_key)
    print(f"voices_read: {'OK' if status == 200 else 'FAILED'} ({status})")
    if status != 200:
        print(json.dumps(body.get("detail", body), ensure_ascii=False)[:500])
        return

    voice_map = {voice.get("voice_id"): voice for voice in body.get("voices", [])}
    for key in VOICE_KEYS:
        voice_id = env.get(key, "")
        if not voice_id:
            print(f"{key}: missing")
            continue
        voice = voice_map.get(voice_id)
        print(f"{key}: {'OK ' + voice.get('name', '') if voice else 'NOT_FOUND'}")
        if args.test_tts and voice:
            output = PROJECT_ROOT / "voices" / f"test-{key.lower()}.mp3"
            tts_status, tts_body = request_tts(api_key, model_id, voice_id, "test", output)
            print(f"  tts: {'OK ' + str(output) if tts_status == 200 else 'FAILED ' + str(tts_status)}")
            if tts_body:
                print("  " + json.dumps(tts_body.get("detail", tts_body), ensure_ascii=False)[:500])


if __name__ == "__main__":
    main()
