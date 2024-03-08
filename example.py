from regex.nodes.LeafRegexNode import LeafRegexNode
from regex.nodes.BinaryRegexNode import BinaryRegexNode, BinaryOperationType
from regex.nodes.UnaryRegexNode import UnaryRegexNode
from automatons.classes import NFA, DFA
from automatons.constructors.RegexToNFA import RegexToNFA
from automatons.constructors.NFAToDFA import NFAToDFA
from automatons.constructors.NFAToMFDFA import NFAToMFDFA

def example():
    # constructing regex = a*(b+c)*ab
    a = LeafRegexNode('a')
    b = LeafRegexNode('b')
    c = LeafRegexNode('c')
    a_star = UnaryRegexNode(a)
    b_plus_c = BinaryRegexNode(b, c, BinaryOperationType.UNITE)
    b_plus_c_star = UnaryRegexNode(b_plus_c)
    reg_1 = BinaryRegexNode(a_star, b_plus_c_star, BinaryOperationType.CONCATENATION)
    reg_2 = BinaryRegexNode(a, b, BinaryOperationType.CONCATENATION)
    regex = BinaryRegexNode(reg_1, reg_2, BinaryOperationType.CONCATENATION)

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