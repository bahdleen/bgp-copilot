import json
import time
import requests
import os
URL = os.getenv("AI_API_URL", "[API excluded by author — insert your endpoint here]")


def extract_between_markers(text: str):
    start = text.find("BEGIN_JSON")
    end = text.find("END_JSON")
    if start == -1 or end == -1 or end <= start:
        return None
    block = text[start + len("BEGIN_JSON"):end].strip()
    return block

def main():
    payload = json.load(open("payload_bgp_outputs.json"))

    timeout_seconds = 420
    retries = 3
    last_err = None

    for attempt in range(1, retries + 1):
        try:
            r = requests.post(URL, json=payload, timeout=timeout_seconds)
            r.raise_for_status()
            resp = r.json()

            summary = resp.get("summary", "") or ""
            block = extract_between_markers(summary)

            if not block:
                print("ERROR: Markers not found. Raw summary below:\n")
                print(summary)
                return

            obj = json.loads(block)
            print(json.dumps(obj, indent=2))
            return

        except Exception as e:
            last_err = e
            print(f"[attempt {attempt}/{retries}] error: {e}")
            time.sleep(2)

    raise SystemExit(f"Failed after {retries} attempts: {last_err}")

if __name__ == "__main__":
    main()
