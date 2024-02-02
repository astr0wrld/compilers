from nodes.expressions.Expression import Expression


class StrExpression(Expression):
    def __init__(
            self,
            word: str
    ) -> None:
        self.str = word

    def accept(self, visitor):
        return visitor.visit_str_expression(self)
