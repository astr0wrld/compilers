from automatons.classes import DFA
from automatons.classes import NFA
from automatons.constructors.NFAToDFA import NFAToDFA
from automatons.constructors.RegexToNFA import RegexToNFA
from regex.nodes.RegexNode import RegexNode


def RegexToMFDFA(regex: RegexNode, terminal=None) -> DFA:
    nfa = RegexToNFA(regex, terminal)
    return NFAToMFDFA(nfa)

def NFAToMFDFA(nfa: NFA) -> DFA:
    dfa = NFAToDFA(nfa)
    dfa.minimize()
    dfa.del_unreach()
    dfa.complete()

    return dfa
