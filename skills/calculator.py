import ast
import operator


class CalculatorSkill:

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
        ast.USub: operator.neg,
    }

    def run(self, user_input):

        try:
            result = self.evaluate(user_input)
            return f"The answer is {result}"

        except Exception:
            return "I couldn't calculate that."

    def evaluate(self, expression):

        node = ast.parse(expression, mode="eval").body

        return self._eval(node)

    def _eval(self, node):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.Num):
            return node.n

        if isinstance(node, ast.BinOp):
            return self.OPERATORS[type(node.op)](
                self._eval(node.left),
                self._eval(node.right)
            )

        if isinstance(node, ast.UnaryOp):
            return self.OPERATORS[type(node.op)](
                self._eval(node.operand)
            )

        raise TypeError(node)