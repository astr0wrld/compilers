from enum import Enum

from regex.nodes.RegexNode import RegexNode
from regex.regex_visitors.Visitor import Visitor

class UnaryRegexNode(RegexNode):
    def __init__(self, node: RegexNode):
        self.node = node

    def __str__(self):
        return f'({self.node})*'

    def accept(self, visitor: Visitor):
        return visitor.visit(self)