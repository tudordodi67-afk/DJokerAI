import json
import os


class MemoryEngine:

    def __init__(self):
        self.folder = "memory"
        self.file = os.path.join(self.folder, "chat_memory.json")

        os.makedirs(self.folder, exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def _load(self):
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_message(self, role, message):
        data = self._load()

        data.append({
            "role": role,
            "message": message
        })

        self._save(data)

    def last_messages(self, count=10):
        return self._load()[-count:]

    def get_history(self):
        return self._load()

    def clear(self):
        self._save([])