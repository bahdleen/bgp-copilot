import json, requests

URL = "https://ai-api.edjenuwahome.uk/v1/analyze"

report = json.load(open("bgp_report.json"))

payload = {
  "input": {
    "task": "Add short network engineer commentary",
    "message": (
      "Write 3-5 bullet points (short) confirming what is healthy here and 2 optional improvements. "
      "No JSON required.\n\n"
      f"Report:\n{json.dumps(report)}"
    )
  }
}

r = requests.post(URL, json=payload, timeout=120)
r.raise_for_status()
resp = r.json()
print(resp.get("summary",""))
