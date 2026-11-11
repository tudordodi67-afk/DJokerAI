class BaseSkill:

    def __init__(self, memory, facts):
        self.memory = memory
        self.facts = facts

    def run(self, user_input):
        raise NotImplementedError