from abc import ABC, abstractmethod
from nodes.Program import Program
from nodes.expressions.AddExpression import AddExpression
from nodes.expressions.BraceExpression import BraceExpression
from nodes.expressions.DivExpression import DivExpression
from nodes.expressions.IdentExpression import IdentExpression
from nodes.expressions.MulExpression import MulExpression
from nodes.expressions.NumberExpression import NumberExpression
from nodes.expressions.BoolExpression import BoolExpression
from nodes.expressions.SubExpression import SubExpression
from nodes.expressions.StrExpression import StrExpression
from nodes.expressions.NotEqualExpression import NotEqualExpression
from nodes.expressions.EqualExpression import EqualExpression
from nodes.expressions.LessExpression import LessExpression
from nodes.expressions.MoreExpression import MoreExpression

from nodes.statements.AssignStatement import AssignStatement
from nodes.statements.PrintStatement import PrintStatement
from nodes.statements.IfStatement import IfStatement
from nodes.statements.WhileStatement import WhileStatement


class Visitor(ABC):
    @abstractmethod
    def visit_program(self, program: Program):
        pass

    @abstractmethod
    def visit_less_expression(self, expression: LessExpression):
        pass

    @abstractmethod
    def visit_more_expression(self, expression: MoreExpression):
        pass

    @abstractmethod
    def visit_if_statement(self, expression: IfStatement):
        pass

    @abstractmethod
    def visit_while_statement(self, expression: WhileStatement):
        pass

    @abstractmethod
    def visit_equal_expression(self, expression: EqualExpression):
        pass

    @abstractmethod
    def visit_notequal_expression(self, expression: NotEqualExpression):
        pass

    @abstractmethod
    def visit_str_expression(self, expression: StrExpression):
        pass

    @abstractmethod
    def visit_bool_expression(self, expression: BoolExpression):
        pass

    @abstractmethod
    def visit_number_expression(self, expression: NumberExpression):
        pass

    @abstractmethod
    def visit_add_expression(self, expression: AddExpression):
        pass

    @abstractmethod
    def visit_sub_expression(self, expression: SubExpression):
        pass

    @abstractmethod
    def visit_mul_expression(self, expression: MulExpression):
        pass

    @abstractmethod
    def visit_div_expression(self, expression: DivExpression):
        pass

    @abstractmethod
    def visit_brace_expression(self, expression: BraceExpression):
        pass

    @abstractmethod
    def visit_assign_statement(self, statement: AssignStatement):
        pass

    @abstractmethod
    def visit_print_statement(self, statement: PrintStatement):
        pass

    @abstractmethod
    def visit_ident_expression(self, expression: IdentExpression):
        pass
