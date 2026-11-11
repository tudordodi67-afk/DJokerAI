import re


class IntentEngine:

    def detect(self, user_input):

        text = user_input.lower().strip()

        # Калькулятор
        if re.fullmatch(r"[0-9\.\+\-\*\/\(\)\s%]+", text):
            return "calculator"

        # Вопрос
        if text.endswith("?"):
            return "question"

        # Обучение
        if " is " in text or " likes " in text:
            return "learn"

        # Обычный разговор
        return "chat"