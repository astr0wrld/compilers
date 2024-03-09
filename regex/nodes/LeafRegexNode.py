from regex.nodes.RegexNode import RegexNode
from regex.regex_visitors.Visitor import Visitor


class LeafRegexNode(RegexNode):
    value: str

    def __init__(self, letter: str = None):
        self.value = letter

    def accept(self, visitor: Visitor):
        return visitor.visit(self)

    def __str__(self):
        return self.value