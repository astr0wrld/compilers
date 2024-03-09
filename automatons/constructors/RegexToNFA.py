from automatons.classes import NFA
from automatons.constructors.nfa_operations import *
from regex.nodes.RegexNode import RegexNode
from regex.nodes.LeafRegexNode import LeafRegexNode
from regex.nodes.UnaryRegexNode import UnaryRegexNode
from regex.nodes.BinaryRegexNode import BinaryRegexNode, BinaryOperationType


def RegexToNFA(regex: RegexNode, terminal=None) -> NFA:
    if isinstance(regex, UnaryRegexNode):
        nfa = nfa_unary(regex)
    elif isinstance(regex, LeafRegexNode):
        nfa = nfa_leaf(regex)
    else:
        nfa = nfa_binary(regex)
    if terminal is not None:
        nfa.trap.make_terminal(terminal)
    return nfa

def nfa_unary(regex: UnaryRegexNode) -> NFA:
    nfa = RegexToNFA(regex.node)
    return nfa_closure(nfa)

def nfa_leaf(regex: LeafRegexNode) -> NFA:
    nfa = NFA()
    nfa.add_edge(nfa.root, nfa.trap, regex.value)
    return nfa

def nfa_binary(regex: BinaryRegexNode) -> NFA:
    first, second = RegexToNFA(regex.exp1), RegexToNFA(regex.exp2)
    if regex.operation == BinaryOperationType.UNITE:
        return nfa_unite([first, second])
    else:
        return nfa_conc(first, second)
