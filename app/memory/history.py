import json
import os
from datetime import datetime
from typing import List, Dict

HISTORY_FILE = "data/history.json"


def load_history() -> List[Dict]:
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_to_history(raw_prompt: str, refined_prompt: str):
    history = load_history()

    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "raw": raw_prompt,
        "refined": refined_prompt
    }

    # En başa ekle (En yeni en üstte)
    history.insert(0, new_entry)

    # Son 50 kaydı tut (Dosya şişmesin)
    history = history[:50]

    # Klasör yoksa oluştur
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)