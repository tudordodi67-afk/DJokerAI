import re


class NLP:

    def normalize(self, text):
        return text.lower().strip()

    def extract_name(self, text):
        patterns = [
            r"my name is (.+)",
            r"i am (.+)",
            r"i'm (.+)"
        ]

        for pattern in patterns:
            match = re.search(pattern, text.lower())
            if match:
                return match.group(1).strip().title()

        return None

    def extract_age(self, text):
        match = re.search(r"(\d+)\s*years? old", text.lower())

        if match:
            return match.group(1)

        return None

    def extract_color(self, text):
        match = re.search(r"favorite color is (.+)", text.lower())

        if match:
            return match.group(1).strip()

        return None