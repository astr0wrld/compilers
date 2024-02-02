from antlr4 import *
from visitors.Visitor import Visitor
import ExprParser
import abc

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


class PrintVisitor(ParseTreeVisitor):
    def __init__(self):
        self.cnt = 0
        self.str = ""

    def Print(self, word: str):
        self.str +=  "      " * self.cnt + word + '\n'

    def visit_program(self, program: Program):
        self.Print("Prorgam\n")
        for expression in program.expressions:
            expression.accept(self)
            self.cnt = 0
            self.Print("\n--------------\n")
    
    def visit_ident_expression(self, expression: IdentExpression):
        self.Print(f"IdentExpression({expression.name})")

    def visit_number_expression(self, expression: NumberExpression):
        self.Print(f"NumberExpression({expression.number})")

    def visit_bool_expression(self, expression: BoolExpression):
        self.Print(f"BooleanExpression({expression.bool})")
    
    def visit_str_expression(self, expression: StrExpression):
        self.Print(f"StringExpression({expression.str})")

    def visit_add_expression(self, expression: AddExpression):
        self.Print(f"AddExpression")
        self.cnt += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.cnt -= 1

    def visit_sub_expression(self, expression: SubExpression):
        self.Print(f"SubExpression")
        self.cnt += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.cnt -= 1

    def visit_mul_expression(self, expression: MulExpression):
        self.Print("MulExpression")
        self.cnt += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.cnt -= 1

    def visit_div_expression(self, expression: DivExpression):
        self.Print("DivExpression")
        self.cnt += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.cnt -= 1

    def visit_brace_expression(self, expression: BraceExpression):
        self.Print("BraceExpression")
        self.cnt += 1
        expression.expression.accept(self)
        self.cnt -= 1

    def visit_more_expression(self, expression: MoreExpression):
         self.Print("MoreExpression")
         self.cnt += 1
         expression.left.accept(self)
         expression.right.accept(self)
         self.cnt -= 1

    def visit_less_expression(self, expression: LessExpression):
        self.Print("LessExpression")
        self.cnt += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.cnt -= 1

    def visit_equal_expression(self, expression: EqualExpression):
        self.Print("EqualExpression")
        self.cnt += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.cnt -= 1

    def visit_notequal_expression(self, expression: NotEqualExpression):
        self.Print("NotEqualExpression")
        self.cnt += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.cnt -= 1

    def visit_assign_statement(self, statement: AssignStatement):
        self.Print("Assign")
        self.cnt += 1
        self.Print(f"IdentExpression({statement.variable})")
        statement.expression.accept(self)
        self.cnt -= 1

    def visit_if_statement(self, statement: IfStatement):
        self.Print("IfStatement")
        self.cnt += 1
        for expression in statement.expressions:
            expression.accept(self)
        self.cnt -= 1

    def visit_while_statement(self, statement: WhileStatement):
        self.Print("WhileStatement")
        self.cnt += 1
        for expression in statement.expressions:
            expression.accept(self)
        self.cnt -= 1
    
    def visit_print_statement(self, statement: PrintStatement):
        self.Print("PrintExpression")
        self.cnt += 1
        statement.expression.accept(self)
        self.cnt -= 1
