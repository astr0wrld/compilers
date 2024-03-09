from __future__ import annotations
from enum import Enum

from regex.nodes.RegexNode import RegexNode
from regex.regex_visitors.Visitor import Visitor


class BinaryOperationType(Enum):
    CONCATENATION = "X"
    UNITE = "+"

class BinaryRegexNode(RegexNode):
    def __init__(self, left: RegexNode, right: RegexNode, operation: BinaryOperationType):
        self.exp1 = left
        self.exp2 = right
        self.operation = operation

    def __str__(self):
        if self.operation == BinaryOperationType.CONCATENATION:
            return f'{self.exp1}{self.exp2}'
        if self.operation == BinaryOperationType.UNITE:
            return f'{self.exp1}+{self.exp2}'

    def accept(self, visitor: Visitor):
        return visitor.visit(self)


