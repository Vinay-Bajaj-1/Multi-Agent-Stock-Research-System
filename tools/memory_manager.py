import json
from pathlib import Path


MEMORY_PATH = Path(
    "memory/history.json"
)


def load_memory():

    if not MEMORY_PATH.exists():
        return []

    try:
        with open(MEMORY_PATH, "r") as f:

            content = f.read().strip()

            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        return []


def save_memory(entry):

    memory = load_memory()

    memory.append(entry)

    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=4)


def get_last_analysis(ticker):
    memory = load_memory()

    filtered = [
        entry for entry in memory
        if entry['ticker'] == ticker
    ]

    if not filtered:
        return None

        
    return filtered[-1]