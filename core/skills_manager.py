import re
from skills.calculator import CalculatorSkill


class SkillsManager:

    def __init__(self, memory, facts):
        self.memory = memory
        self.facts = facts
        self.calculator = CalculatorSkill()

    def execute(self, intent, text):

        text = text.strip()

        # -----------------------------------
        # Calculator
        # -----------------------------------

        if intent == "calculator":
            return self.calculator.run(text)

        # -----------------------------------
        # Who is X?
        # -----------------------------------

        m = re.fullmatch(r"who is (.+?)\??", text, re.IGNORECASE)

        if m:

            subject = m.group(1).strip()

            facts = self.facts.search(subject=subject)

            if facts:

                answers = []

                for fact in facts:

                    relation = fact["relation"].replace("_", " ")

                    if relation == "is":
                        answers.append(
                            f"{fact['subject']} is {fact['object']}."
                        )
                    else:
                        answers.append(
                            f"{fact['subject']} {relation} {fact['object']}."
                        )

                return "\n".join(answers)

        # -----------------------------------
        # Where is X from?
        # -----------------------------------

        m = re.fullmatch(r"where is (.+?) from\??", text, re.IGNORECASE)

        if m:

            subject = m.group(1).strip()

            facts = self.facts.search(
                subject=subject,
                relation="from"
            )

            if facts:
                return f"{facts[0]['subject']} is from {facts[0]['object']}."

        # -----------------------------------
        # What does X like?
        # -----------------------------------

        m = re.fullmatch(r"what does (.+?) like\??", text, re.IGNORECASE)

        if m:

            subject = m.group(1).strip()

            facts = self.facts.search(
                subject=subject,
                relation="likes"
            )

            if facts:
                return f"{facts[0]['subject']} likes {facts[0]['object']}."

        # -----------------------------------
        # Who leads X?
        # -----------------------------------

        m = re.fullmatch(r"who leads (.+?)\??", text, re.IGNORECASE)

        if m:

            group = m.group(1).strip()

            facts = self.facts.search(
                relation="leader_of",
                obj=group
            )

            if facts:
                return f"{facts[0]['subject']} leads {facts[0]['object']}."

        # -----------------------------------
        # Where does X live?
        # -----------------------------------

        m = re.fullmatch(r"where does (.+?) live\??", text, re.IGNORECASE)

        if m:

            subject = m.group(1).strip()

            facts = self.facts.search(
                subject=subject,
                relation="lives_in"
            )

            if facts:
                return f"{facts[0]['subject']} lives in {facts[0]['object']}."

        return None