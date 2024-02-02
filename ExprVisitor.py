# Generated from Expr.g4 by ANTLR 4.13.0
from antlr4 import *
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


class ExprVisitor(ParseTreeVisitor):
    def visitProg(self, ctx):
        statements = []
        for statement in ctx.stmt():
            statements.append(self.visit(statement))
        return Program(expressions=statements)

    def visitStmt(self, ctx):
        if ctx.assign is not None:
            return AssignStatement(ctx.ident.text, self.visit(ctx.assign))
        elif ctx.if_condition is not None:
            statements = []
            for statement in ctx.stmt():
                statements.append(self.visit(statement))
            condition = self.visit(ctx.if_condition)
            return IfStatement(condition, statements)

        elif ctx.while_condition is not None:
            statements = []
            for statement in ctx.stmt():
                statements.append(statement)
            condition = self.visit(ctx.while_condition)
            return WhileStatement(condition, statements)
        else:
            return PrintStatement(self.visit(ctx.printexp))

    def visitExpr(self, ctx):

        if ctx.string is not None:
            return StrExpression(ctx.string.text[1:-1])

        if ctx.ident is not None:
            return IdentExpression(ctx.ident.text)

        if ctx.value is not None:
            return NumberExpression(ctx.value.text)

        if ctx.bool_ is not None:
            return BoolExpression(ctx.bool_.text)

        if ctx.exp is not None:
            return BraceExpression(self.visit(ctx.exp))

        if ctx.op.text == '/':
            return DivExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '*':
            return MulExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '+':
            return AddExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '-':
            return SubExpression(self.visit(ctx.left), self.visit(ctx.right))

        elif ctx.op.text == '>':
            return MoreExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '<':
            return LessExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '==':
            return EqualExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '!=':
            return NotEqualExpression(self.visit(ctx.left), self.visit(ctx.right))



