from automatons.classes import DFA
from automatons.classes import NFA
from automatons.nodes import DFA_Node
from automatons.nodes import NFA_Node


def get_next(begin: set[NFA_Node], letter: str) -> set[NFA_Node]:
    final = set()
    for node in begin:
        if letter in node.transitions.keys():
            final = final.union(node.transitions[letter])

    return final


def get_letters(dfa: DFA, cur) -> set:
    letters = set()
    for vertex in cur:
        for letter in vertex.transitions.keys():
            if letter is not None:
                dfa.alphabet.add(letter)
                letters.add(letter)

    return letters


def NFAToDFA(nfa: NFA) -> DFA:
    nfa.del_eps()
    dfa_nodes = []
    transitions = dict()
    dfa_nodes.append(frozenset([nfa.root]))
    q = [frozenset([nfa.root])]
    used = set()
    dfa = DFA()
    eq = dict()

    while len(q) != 0:
        cur_state = q.pop(0)
        letters = get_letters(dfa, cur_state)

        for letter in letters:
            next_state = frozenset(get_next(cur_state, letter))
            if cur_state not in transitions.keys():
                transitions[cur_state] = dict()
            transitions[cur_state][letter] = next_state

            if next_state not in used:
                dfa_nodes.append(next_state)
                used.add(next_state)
                q.append(next_state)
    
    for node in dfa_nodes:
        if nfa.root in node:
            dfa.root = DFA_Node(node)
            eq[node] = dfa.root
        else:
            new_node = DFA_Node(node)
            eq[node] = new_node
            dfa.states.add(new_node)

        for vert in node:
            for term_state in vert.terminals:
                eq[node].terminals.add(term_state)

    for source, letter_transitions in transitions.items():
        for letter, target in letter_transitions.items():
            dfa.add_edge(eq[source], eq[target], letter)

    dfa.del_unreach()

    return dfa

