from __future__ import annotations

import argparse
import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from common import PROJECT_ROOT, load_env, load_json, save_json


def scene_prompt(scene: dict[str, Any], episode: dict[str, Any]) -> str:
    return "\n".join(
        [
            scene["visual_prompt"],
            "",
            "Production requirements:",
            "- Vertical 9:16 TikTok frame.",
            "- No visible captions, no readable text, no logos, no copyrighted characters.",
            "- Original 3D animated family movie look with anthropomorphic fruit-headed characters.",
            "- No human faces or realistic human heads; the comedy comes from fruit personalities and the situation.",
            "- Leave clear lower-third space for subtitles.",
            f"- Episode: {episode.get('title', '')}. Scene type: {scene.get('type', '')}.",
        ]
    )


def find_base64_image(payload: Any) -> tuple[str, str] | None:
    if isinstance(payload, dict):
        if isinstance(payload.get("output_image"), dict) and payload["output_image"].get("data"):
            return payload["output_image"]["data"], payload["output_image"].get("mime_type", "image/png")
        if payload.get("data") and (
            "image" in str(payload.get("mime_type", "")).lower()
            or "image" in str(payload.get("mimeType", "")).lower()
        ):
            return payload["data"], payload.get("mime_type") or payload.get("mimeType") or "image/png"
        inline = payload.get("inlineData") or payload.get("inline_data")
        if isinstance(inline, dict) and inline.get("data"):
            return inline["data"], inline.get("mimeType") or inline.get("mime_type") or "image/png"
        for value in payload.values():
            found = find_base64_image(value)
            if found:
                return found
    elif isinstance(payload, list):
        for item in payload:
            found = find_base64_image(item)
            if found:
                return found
    return None


def post_json(url: str, headers: dict[str, str], payload: dict[str, Any]) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def generate_with_interactions(api_key: str, model: str, prompt: str) -> tuple[bytes, str, dict[str, Any]]:
    data = post_json(
        "https://generativelanguage.googleapis.com/v1beta/interactions",
        {"x-goog-api-key": api_key},
        {"model": model, "input": [{"type": "text", "text": prompt}]},
    )
    found = find_base64_image(data)
    if not found:
        raise RuntimeError("Gemini Interactions response did not include an image.")
    encoded, mime_type = found
    return base64.b64decode(encoded), mime_type, data


def generate_with_generate_content(api_key: str, model: str, prompt: str) -> tuple[bytes, str, dict[str, Any]]:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    data = post_json(
        url,
        {},
        {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
        },
    )
    found = find_base64_image(data)
    if not found:
        raise RuntimeError("Gemini generateContent response did not include an image.")
    encoded, mime_type = found
    return base64.b64decode(encoded), mime_type, data


def extension_for_mime(mime_type: str) -> str:
    if "jpeg" in mime_type or "jpg" in mime_type:
        return ".jpg"
    if "webp" in mime_type:
        return ".webp"
    return ".png"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_json", type=Path)
    parser.add_argument("--limit", type=int, default=0, help="Limit number of scenes. 0 means all scenes.")
    parser.add_argument("--run", action="store_true", help="Actually call Gemini and generate images. Without this, only prompt files are written.")
    parser.add_argument("--api", choices=["interactions", "generate-content"], default="generate-content")
    parser.add_argument("--model", help="Override GEMINI_IMAGE_MODEL.")
    args = parser.parse_args()

    env = load_env()
    api_key = env.get("GEMINI_API_KEY", "")
    model = args.model or env.get("GEMINI_IMAGE_MODEL", "gemini-3.1-flash-lite-image")
    episode = load_json(args.episode_json)
    episode_slug = args.episode_json.stem
    output_dir = PROJECT_ROOT / "assets" / "generated" / episode_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    scenes = episode.get("scenes", [])
    if args.limit:
        scenes = scenes[: args.limit]

    manifest: list[dict[str, Any]] = []
    for index, scene in enumerate(scenes, start=1):
        prompt = scene_prompt(scene, episode)
        prompt_path = output_dir / f"{index:02}-{scene['id']}.prompt.txt"
        prompt_path.write_text(prompt, encoding="utf-8")
        record: dict[str, Any] = {
            "scene_id": scene["id"],
            "prompt_file": str(prompt_path.relative_to(PROJECT_ROOT)),
            "model": model,
            "generated": False,
        }
        if args.run:
            if not api_key:
                sys.exit("Missing GEMINI_API_KEY in .env")
            try:
                if args.api == "interactions":
                    image_bytes, mime_type, raw = generate_with_interactions(api_key, model, prompt)
                else:
                    image_bytes, mime_type, raw = generate_with_generate_content(api_key, model, prompt)
            except urllib.error.HTTPError as error:
                detail = error.read().decode("utf-8", errors="replace")
                sys.exit(f"Gemini image generation failed ({error.code}): {detail}")
            except Exception as error:
                sys.exit(f"Gemini image generation failed: {error}")

            image_path = output_dir / f"{index:02}-{scene['id']}{extension_for_mime(mime_type)}"
            image_path.write_bytes(image_bytes)
            debug_path = output_dir / f"{index:02}-{scene['id']}.response.json"
            save_json(debug_path, raw)
            record.update(
                {
                    "generated": True,
                    "image_file": str(image_path.relative_to(PROJECT_ROOT)),
                    "mime_type": mime_type,
                    "response_file": str(debug_path.relative_to(PROJECT_ROOT)),
                }
            )
            print(image_path)
        else:
            print(f"DRY_RUN {prompt_path}")
        manifest.append(record)

    save_json(output_dir / "manifest.json", manifest)
    print(output_dir / "manifest.json")


if __name__ == "__main__":
    main()
