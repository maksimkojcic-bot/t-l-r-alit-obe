from __future__ import annotations

import json
import urllib.error
import urllib.request

from common import load_env


def main() -> None:
    env = load_env()
    api_key = env.get("GEMINI_API_KEY", "")
    print(f"GEMINI_API_KEY: {'set len=' + str(len(api_key)) if api_key else 'missing'}")
    if not api_key:
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = {"raw": body[:500]}
        print(f"gemini_models: FAILED ({error.code})")
        print(json.dumps(parsed.get("error", parsed), ensure_ascii=False)[:600])
        return

    models = data.get("models", [])
    names = [model.get("name", "") for model in models[:8]]
    print(f"gemini_models: OK ({len(models)} models visible)")
    for name in names:
        print(f"  {name}")


if __name__ == "__main__":
    main()
