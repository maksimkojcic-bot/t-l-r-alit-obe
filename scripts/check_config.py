from __future__ import annotations

from common import PROJECT_ROOT, load_env


REQUIRED_FOR_TEXT = ["GEMINI_API_KEY"]
REQUIRED_FOR_VOICE = [
    "ELEVENLABS_API_KEY",
    "VOICE_HOST",
    "VOICE_COACH",
    "VOICE_CANDIDATE_1",
    "VOICE_CANDIDATE_2",
    "VOICE_CANDIDATE_3",
    "VOICE_CANDIDATE_4",
    "VOICE_CANDIDATE_5",
]


def status(value: str) -> str:
    if not value or value.startswith("REMPLACE_"):
        return "missing"
    return f"set len={len(value)}"


def main() -> None:
    env_path = PROJECT_ROOT / ".env"
    env = load_env()
    print(f"env_file: {'present' if env_path.exists() else 'missing'}")
    print("Gemini:")
    for key in REQUIRED_FOR_TEXT:
        print(f"  {key}: {status(env.get(key, ''))}")
    print("ElevenLabs:")
    for key in REQUIRED_FOR_VOICE:
        print(f"  {key}: {status(env.get(key, ''))}")
    print("Publishing:")
    for key in ["TIKTOK_CLIENT_KEY", "TIKTOK_ACCESS_TOKEN"]:
        print(f"  {key}: {status(env.get(key, ''))}")


if __name__ == "__main__":
    main()
