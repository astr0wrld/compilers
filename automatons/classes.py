from automatons.nodes import BasicNode
from automatons.nodes import DFA_Node
from automatons.nodes import NFA_Node


class BasicAut:
    def __init__(self, alphabet=None):
        self.root = BasicNode()
        self.states = set()
        self.alphabet = alphabet if alphabet is not None else set()

    def add_nodes(self, auts):
        for aut in auts:
            for state in aut.states:
                self.states.add(state)


class DFA(BasicAut):
    def __init__(self):
        super().__init__()
        self.root = DFA_Node()
        self.trap = DFA_Node()
        self.states.add(self.root)
        self.states.add(self.trap)

    def add_edge(self, first: DFA_Node, second: DFA_Node, letter: str):
        self.states.add(first)
        self.states.add(second)
        self.alphabet.add(letter)
        first.transitions[letter] = second

    def merge_states(self, merge_states: set):
        new_state = DFA_Node()
        self.states.add(new_state)
        if self.root in merge_states:
            self.root = new_state

        for state in self.states:
            for letter, target in state.transitions.items():
                if target in merge_states:
                    state.transitions[letter] = new_state

        for state in merge_states:
            for letter, target in state.transitions.items():
                if target in merge_states:
                    new_state.transitions[letter] = new_state
                else:
                    new_state.transitions[letter] = target

            if state in self.states:
                self.states.remove(state)
            
            for term_state in state.terminals:
                new_state.terminals.add(term_state)

    def minimize(self):
        eq_classes = dict()
        for first in self.states:
            for second in self.states:
                if first != second and first.transitions == second.transitions and first.terminals == second.terminals:
                    if id(first) in eq_classes.keys():
                        eq_classes[id(first)].add(second)
                    else:
                        eq_classes[id(first)] = set()
                        eq_classes[id(first)].add(first)
                        eq_classes[id(first)].add(second)

        for _, states in eq_classes.items():
            self.merge_states(states)

    def complete(self):
        for letter in self.alphabet:
            self.add_edge(self.trap, self.trap, letter)
        for tmp in self.states:
            for letter in self.alphabet:
                if letter not in tmp.transitions.keys():
                    self.add_edge(tmp, self.trap, letter)

    def del_unreach(self):
        used = set()
        used.add(self.root)
        q = [self.root] 
        while len(q) != 0:
            cur = q.pop(0)
            for _, tmp in cur.transitions.items():
                if tmp not in used:
                    used.add(tmp)
                    q.append(tmp)
        states_copy = self.states.copy()              
        for tmp in states_copy:
            if tmp not in used:
                self.states.remove(tmp)

    def print(self):
        print("number of states:", len(self.states))
        print("alphabet:", *sorted(self.alphabet))
        for state in self.states:
            if state == self.root:
                print("root state:", end=" ")
            elif state == self.trap:
                print("trap state:", end=" ")
            else:
                print("state:", end=" ")
            print(state, *state.terminals)
            print("transitions: ", end=" ")
            for letter, to in sorted(state.transitions.items()):
                print(f"{letter}: {str(to)}", end=" ")
            print('\n')


class NFA(BasicAut):
    def __init__(self):
        super().__init__()
        self.root = NFA_Node()
        self.trap = NFA_Node()
        self.states.add(self.root)
        self.states.add(self.trap)

    def add_edge(self, first: NFA_Node, second: NFA_Node, letter: str):
        self.states.add(first)
        self.states.add(second)
        self.alphabet.add(letter)
        if letter not in first.transitions.keys():
            first.transitions[letter] = set()
        first.transitions[letter].add(second)

    def del_unreach(self):
        used = set()
        used.add(self.root)
        q = [self.root]
        while len(q) != 0:
            cur = q.pop(0)
            for _, tmps in cur.transitions.items():
                for tmp in tmps:
                    if tmp not in used:
                        used.add(tmp)
                        q.append(tmp)    
        states_copy = self.states.copy()              
        for tmp in states_copy:
            if tmp not in used:
                self.states.remove(tmp)

    def get_eps(self) -> list:
        pairs = []
        for first in self.states:
            for second in first.eps_closure:
                pairs.append([first, second])
        return pairs

    def del_eps(self):
        while len(self.get_eps()) != 0:
            pairs = self.get_eps()
            for first, second in pairs:
                for term_state in second.terminals:
                    first.terminals.add(term_state)
                for letter, states in second.transitions.items():
                    for state in states:
                        self.add_edge(first, state, letter)
                for tmp in second.eps_closure:
                    first.eps_closure.add(tmp)
                first.eps_closure.remove(second)
        self.del_unreach()

    def print(self):
        print("number of states:", len(self.states))
        print("alphabet:", *sorted(self.alphabet))
        for state in self.states:
            if state == self.root:
                print("root state:", end=" ")
            elif state == self.trap:
                print("trap state:", end=" ")
            else:
                print("state:", end=" ")
            print(state, *state.terminals)
            print("transitions: ", end=" ")
            for letter, to in sorted(state.transitions.items()):
                print(f"{letter}: {[str(vertex) for vertex in to]}", end=" ")
            print()
            print("eps_closure: ", [str(vertex) for vertex in state.eps_closure])
            print('\n')