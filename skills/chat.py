from skills.base_skill import BaseSkill
from skills.memory import MemorySkill


class ChatSkill(BaseSkill):

    def __init__(self, memory, facts):
        super().__init__(memory, facts)
        self.memory_skill = MemorySkill(facts)

    def run(self, user_input):

        text = user_input.lower()

        # -----------------------
        # Самообучение
        # -----------------------

        key, value = self.memory_skill.learn(user_input)

        if key:
            return f"I'll remember your {key.replace('_',' ')} is {value}."

        # -----------------------
        # Приветствие
        # -----------------------

        if any(x in text for x in [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good evening"
        ]):
            return "Hello! I'm DJoker AI."

        # -----------------------
        # Как дела
        # -----------------------

        if "how are you" in text:
            return "I'm doing great."

        # -----------------------
        # Имя
        # -----------------------

        if any(x in text for x in [
            "what is my name",
            "who am i",
            "my name"
        ]):

            name = self.facts.recall("name")

            if name:
                return f"Your name is {name}."

        # -----------------------
        # Возраст
        # -----------------------

        if "how old am i" in text:

            age = self.facts.recall("age")

            if age:
                return f"You are {age} years old."

        # -----------------------
        # Цвет
        # -----------------------

        if "favorite color" in text:

            color = self.facts.recall("favorite_color")

            if color:
                return f"Your favorite color is {color}."

        # -----------------------
        # Работа
        # -----------------------

        if "my job" in text:

            job = self.facts.recall("job")

            if job:
                return f"You work as {job}."

        # -----------------------
        # Что ты знаешь
        # -----------------------

        if any(x in text for x in [
            "what do you know",
            "what do you remember"
        ]):

            data = self.facts.all()

            if not data:
                return "I don't know anything yet."

            answer = "Here's what I know:\n\n"

            for key, value in data.items():
                answer += f"{key}: {value}\n"

            return answer

        # ---------------------------------
        # Очень важно
        # ---------------------------------

        # Если дошли сюда,
        # значит ChatSkill ответа НЕ знает.

        return None