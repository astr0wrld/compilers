import sys
from antlr4 import *
from nodes.Program import Program
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from visitors.InterpeterVisitor import InterpreterVisitor
from visitors.PrintVisitor import PrintVisitor


def main(argv):
    input_stream = FileStream('input_driver.txt')
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    ast_tree: Program = ExprVisitor().visit(tree)

    interpeter = InterpreterVisitor()
    interpeter.visit_program(ast_tree)

    printer = PrintVisitor()
    printer.visit_program(ast_tree)
    with open("output_driver.txt", "w") as output:
        output.write(printer.str)


if __name__ == '__main__':
    main(sys.argv)