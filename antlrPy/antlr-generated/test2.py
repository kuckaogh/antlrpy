from antlr3 import *;
from antlr3.tree import *;
import Eval
import ExprLexer
import ExprParser
import sys


def evaluate(value):
    input = ANTLRStringStream(value)
    lexer = ExprLexer.ExprLexer(input);
    tokens = CommonTokenStream(lexer);
    parser = ExprParser.ExprParser(tokens);
    r = parser.prog();
    t = r.tree; # // get tree from parser
    nodes = CommonTreeNodeStream(t);
    walker = Eval.Eval(nodes); # // create a tree parser
    return walker.prog()


s="X=6 % 3+X % "

answer = evaluate(s)

raw_input("Press enter to continue")
       