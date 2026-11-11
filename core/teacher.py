import re


class Teacher:

    def __init__(self, facts):
        self.facts = facts

    def learn(self, text):

        text = text.strip()

        # Не обучаемся на вопросах
        if text.endswith("?"):
            return None

        patterns = [

            # X is from Y
            (
                r"(.+?)\s+is\s+from\s+(.+)",
                lambda m: (
                    m.group(1),
                    "from",
                    m.group(2)
                )
            ),

            # X likes Y
            (
                r"(.+?)\s+likes\s+(.+)",
                lambda m: (
                    m.group(1),
                    "likes",
                    m.group(2)
                )
            ),

            # X works at Y
            (
                r"(.+?)\s+works\s+at\s+(.+)",
                lambda m: (
                    m.group(1),
                    "works_at",
                    m.group(2)
                )
            ),

            # X lives in Y
            (
                r"(.+?)\s+lives\s+in\s+(.+)",
                lambda m: (
                    m.group(1),
                    "lives_in",
                    m.group(2)
                )
            ),

            # X is leader of Y
            (
                r"(.+?)\s+is\s+leader\s+of\s+(.+)",
                lambda m: (
                    m.group(1),
                    "leader_of",
                    m.group(2)
                )
            ),

            # Универсальное правило:
            # X is Y
            (
                r"(.+?)\s+is\s+(.+)",
                lambda m: (
                    m.group(1),
                    "is",
                    m.group(2)
                )
            )
        ]

        for pattern, parser in patterns:

            match = re.fullmatch(pattern, text, re.IGNORECASE)

            if match:

                subject, relation, obj = parser(match)

                self.facts.remember(
                    subject.strip(),
                    relation.strip(),
                    obj.strip()
                )

                return (
                    f"I learned:\n"
                    f"{subject.strip()} "
                    f"[{relation.strip()}] "
                    f"{obj.strip()}"
                )

        return None