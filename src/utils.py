from datetime import datetime
import json

def log(message="", level="INFO"):
    print(f"[BlockBreakerClient] [{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[11:-3]}] [{level}] {message}")

def load() -> dict:
    return json.loads(open(f"data.json").read())

def save(jsonData: dict):
    with open(f"data.json", "w") as file:
        json.dump(jsonData, file, indent=4)