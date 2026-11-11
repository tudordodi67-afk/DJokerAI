from core.intent import IntentEngine
from core.nlp import NLP
from core.memory_engine import MemoryEngine
from core.facts_engine import FactsEngine
from core.skills_manager import SkillsManager
from core.ollama_engine import OllamaEngine
from core.teacher import Teacher


class Brain:

    def __init__(self):

        self.intent = IntentEngine()
        self.nlp = NLP()

        self.memory = MemoryEngine()
        self.facts = FactsEngine()

        self.teacher = Teacher(self.facts)

        self.skills = SkillsManager(
            self.memory,
            self.facts
        )

        self.ollama = OllamaEngine()

    def process(self, user_input):

        user_input = user_input.strip()

        # ---------- Сохраняем сообщение ----------
        self.memory.add_message(
            "user",
            user_input
        )

        # ---------- Обучение ----------
        learned = self.teacher.learn(user_input)

        if learned:

            self.memory.add_message(
                "assistant",
                learned
            )

            return learned

        # ---------- Поиск ответа в памяти ----------
        intent = self.intent.detect(user_input)

        response = self.skills.execute(
            intent,
            user_input
        )

        if response:

            self.memory.add_message(
                "assistant",
                response
            )

            return response

        # ---------- Если знаний нет → Ollama ----------
        facts = self.facts.all()

        prompt = """
You are DJoker AI.

You are the personal AI assistant of Fiodor.

Never say you are ChatGPT.
Never say you are created by OpenAI.

If you don't know something,
say:

"I don't know yet."

Never invent facts.

Known knowledge:

"""

        for fact in facts:

            prompt += (
                f"- {fact['subject']} "
                f"{fact['relation']} "
                f"{fact['object']}\n"
            )

        prompt += f"""

User:
{user_input}

Assistant:
"""

        response = self.ollama.ask(prompt)

        self.memory.add_message(
            "assistant",
            response
        )

        return response