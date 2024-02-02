from automatons.classes import NFA

def nfa_closure(aut : NFA) -> NFA:
    new_nfa = NFA()
    new_nfa.root.eps_closure.add(aut.root)
    new_nfa.trap.eps_closure.add(aut.root)
    new_nfa.root.eps_closure.add(new_nfa.trap)
    aut.trap.eps_closure.add(new_nfa.trap)
    new_nfa.trap.terminals = aut.trap.terminals
    new_nfa.add_nodes([aut])
    return new_nfa

def nfa_unite(nfas : list[NFA]) -> NFA:
    new_nfa = NFA()
    for nfa in nfas:
        new_nfa.root.eps_closure.add(nfa.root)
        nfa.trap.eps_closure.add(new_nfa.trap)
    new_nfa.add_nodes(nfas)
    return new_nfa

def nfa_conc(first : NFA, second : NFA) -> NFA:
    new_nfa = NFA()
    new_nfa.root.eps_closure.add(first.root)
    first.trap.eps_closure.add(second.root)
    second.trap.eps_closure.add(new_nfa.trap)
    new_nfa.trap.terminals = second.trap.terminals
    new_nfa.add_nodes([first, second])
    return new_nfa
