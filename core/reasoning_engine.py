class ReasoningEngine:

    def __init__(self, facts):
        self.facts = facts

    def answer(self, question):

        q = question.lower().strip(" ?")

        # Who leads XXX?
        if q.startswith("who leads "):

            target = q.replace("who leads ", "").strip()

            for fact in self.facts.all():

                if (
                    "leader" in fact["object"].lower()
                    and target.lower() in fact["object"].lower()
                ):
                    return fact["subject"]

        # Who is XXX?
        if q.startswith("who is "):

            target = q.replace("who is ", "").strip()

            for fact in self.facts.all():

                if fact["subject"] == target:
                    return fact["object"]

        # What is XXX?
        if q.startswith("what is "):

            target = q.replace("what is ", "").strip()

            for fact in self.facts.all():

                if fact["subject"] == target:
                    return fact["object"]

        return None