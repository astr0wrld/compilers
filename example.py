from regex_to_tree import build_tree
from regex.nodes.LeafRegexNode import LeafRegexNode
from regex.nodes.BinaryRegexNode import BinaryRegexNode, BinaryOperationType
from regex.nodes.UnaryRegexNode import UnaryRegexNode
from automatons.classes import NFA, DFA
from automatons.constructors.RegexToNFA import RegexToNFA
from automatons.constructors.NFAToDFA import NFAToDFA
from automatons.constructors.NFAToMFDFA import NFAToMFDFA

import sys

# Example of correct regexpr: (a*b*(a+c))*+b
# Do not use spaces between symbols

def example():
    if len(sys.argv) > 1:
        regex = build_tree(sys.argv[1])
    else:
        regex = build_tree('a*(b+c)*ab')

    print('-' * 20)
    print("NFA for regex:")
    nfa = RegexToNFA(regex, 'terminal')
    nfa.print()
    print('-' * 20)

    print("DFA from NFA:")
    dfa = NFAToDFA(nfa)
    dfa.print()
    print('-' * 20)

    
    print("MFDFA from NFA:")
    dfa = NFAToMFDFA(nfa)
    dfa.print()
    print('-' * 20)

example()