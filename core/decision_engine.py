import re


class DecisionEngine:

    def __init__(self, facts):

        self.facts = facts

    def search(self, text):

        text = text.lower().strip()

        # Проверяем точное совпадение
        answer = self.facts.recall(text)

        if answer:
            return answer

        # Ищем ключевые слова в вопросе
        words = re.findall(r"\b[a-zA-Z0-9_]+\b", text)

        for word in words:

            answer = self.facts.recall(word)

            if answer:
                return answer

        return None