import re


class MemorySkill:

    def __init__(self, facts):
        self.facts = facts

    def learn(self, text):

        patterns = {
            "name": [
                r"my name is (.+)",
                r"my name's (.+)",
                r"call me (.+)",
                r"i am (.+)"
            ],

            "country": [
                r"i live in (.+)",
                r"my country is (.+)",
                r"i'm from (.+)"
            ],

            "city": [
                r"i live in the city of (.+)",
                r"my city is (.+)"
            ],

            "age": [
                r"i am (\d+) years old",
                r"i am (\d+)"
            ],

            "favorite_game": [
                r"my favorite game is (.+)",
                r"i like playing (.+)"
            ],

            "favorite_food": [
                r"my favorite food is (.+)"
            ],

            "favorite_color": [
                r"my favorite color is (.+)"
            ],

            "job": [
                r"i work as (.+)",
                r"my job is (.+)"
            ]
        }

        text = text.strip()

        for key, regex_list in patterns.items():

            for regex in regex_list:

                match = re.search(regex, text, re.IGNORECASE)

                if match:

                    value = match.group(1).strip()

                    self.facts.remember(key, value)

                    return key, value

        return None, None