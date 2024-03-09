class BasicNode:
    def __init__(self):
        self.transitions = dict()
        self.terminals = set()

    def make_terminal(self, token: str):
        self.terminals.add(token)
    
    def __str__(self):
        return hex(id(self))[-4:]


class DFA_Node(BasicNode):
    def __init__(self, nfa_nodes_set=None):
        super().__init__()
        if nfa_nodes_set is not None:
            for node in nfa_nodes_set:
                for token in node.terminals:
                    self.terminals.add(token)

    
class NFA_Node(BasicNode):
    def __init__(self):
        super().__init__()
        self.eps_closure = set()
