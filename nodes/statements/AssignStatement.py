from nodes.expressions.Expression import Expression


class AssignStatement:
    def __init__(
            self,
            variable: str,
            expression: Expression
    ) -> None:
        self.variable = variable
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_assign_statement(self)
