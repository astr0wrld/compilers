from nodes.expressions.Expression import Expression


class NumberExpression(Expression):
    def __init__(self, number: str) -> None:
        self.number = int(number)

    def accept(self, visitor):
        return visitor.visit_number_expression(self)