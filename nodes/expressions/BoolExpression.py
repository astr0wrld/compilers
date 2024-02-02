from nodes.expressions.Expression import Expression


class BoolExpression(Expression):
    def __init__(
            self,
            expression: str
    ) -> None:
        self.bool = True if expression == 'true' else False

    def __bool__(self):
        return self.bool 

    def accept(self, visitor):
        return visitor.visit_bool_expression(self)
