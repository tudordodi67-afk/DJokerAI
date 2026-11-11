import json
import os


class FactsEngine:

    def __init__(self):
        self.folder = "memory"
        self.file = os.path.join(self.folder, "knowledge.json")

        os.makedirs(self.folder, exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def _load(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def _save(self, data):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def remember(self, subject, relation, obj):

        fact = {
            "subject": subject.strip(),
            "relation": relation.strip(),
            "object": obj.strip()
        }

        data = self._load()

        for item in data:
            if (
                item["subject"].lower() == fact["subject"].lower()
                and item["relation"].lower() == fact["relation"].lower()
                and item["object"].lower() == fact["object"].lower()
            ):
                return

        data.append(fact)
        self._save(data)

    def search_subject(self, subject):

        subject = subject.lower()

        return [
            x for x in self._load()
            if x["subject"].lower() == subject
        ]

    def search_relation(self, relation):

        relation = relation.lower()

        return [
            x for x in self._load()
            if x["relation"].lower() == relation
        ]

    def search_object(self, obj):

        obj = obj.lower()

        return [
            x for x in self._load()
            if x["object"].lower() == obj
        ]

    def search(self, subject=None, relation=None, obj=None):

        results = []

        for fact in self._load():

            if subject and fact["subject"].lower() != subject.lower():
                continue

            if relation and fact["relation"].lower() != relation.lower():
                continue

            if obj and fact["object"].lower() != obj.lower():
                continue

            results.append(fact)

        return results

    def all(self):
        return self._load()

    def clear(self):
        self._save([])