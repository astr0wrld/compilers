from nodes.expressions.Expression import Expression


class LessExpression(Expression):
    def __init__(
            self,
            left: Expression,
            right: Expression
    ) -> None:
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_less_expression(self)
