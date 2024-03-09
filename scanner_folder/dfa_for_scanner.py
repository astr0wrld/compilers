from automatons.classes import DFA
from regex.nodes.UnaryRegexNode import UnaryRegexNode
from regex.nodes.BinaryRegexNode import BinaryRegexNode, BinaryOperationType
from regex.nodes.LeafRegexNode import LeafRegexNode
from automatons.constructors.RegexToNFA import RegexToNFA
from automatons.constructors.nfa_operations import nfa_unite
from automatons.constructors.NFAToMFDFA import NFAToMFDFA
from scanner_folder.classes import ALPHABET, TOKENS


def var_regex() -> BinaryRegexNode:
    letters = LeafRegexNode()
    for letter in ALPHABET['STR']:
        letters = BinaryRegexNode(letters, LeafRegexNode(letter), BinaryOperationType.UNITE)
    var_regex = BinaryRegexNode(letters, UnaryRegexNode(letters), BinaryOperationType.CONCATENATION)
    return var_regex

def space_regex() -> BinaryRegexNode:
    spaces = LeafRegexNode()
    for space in ALPHABET['SPACE']:
        spaces = BinaryRegexNode(spaces, LeafRegexNode(space), BinaryOperationType.UNITE)
    space_reg = BinaryRegexNode(spaces, UnaryRegexNode(spaces), BinaryOperationType.CONCATENATION)
    return space_reg

def num_regex() -> BinaryRegexNode:
    nums = LeafRegexNode()
    for num in ALPHABET['NUM']:
        if num != '0':
            nums = BinaryRegexNode(nums, LeafRegexNode(num), BinaryOperationType.UNITE)
    num_reg = BinaryRegexNode(nums,
                                UnaryRegexNode(BinaryRegexNode(nums, LeafRegexNode('0'), BinaryOperationType.UNITE)),
                                BinaryOperationType.CONCATENATION)
    return num_reg

def str_regex():
    symbols = BinaryRegexNode(var_regex(), num_regex(), BinaryOperationType.UNITE)
    return BinaryRegexNode(LeafRegexNode("'"),
                           BinaryRegexNode(UnaryRegexNode(symbols), LeafRegexNode("'"), BinaryOperationType.CONCATENATION),
                           BinaryOperationType.CONCATENATION)

TOKENS_REGEXPS = {
    'SPACE': space_regex(),
    'VARNAME': var_regex(),
    'NUM': num_regex(),
    'L_FIGURE_BR': LeafRegexNode(ALPHABET['L_FIGURE_BR']),
    'R_FIGURE_BR': LeafRegexNode(ALPHABET['R_FIGURE_BR']),
    'L_ROUND_BR': LeafRegexNode(ALPHABET['L_ROUND_BR']),
    'R_ROUND_BR': LeafRegexNode(ALPHABET['R_ROUND_BR']),
    'QUOTE': LeafRegexNode(ALPHABET['QUOTE']),
    'SEMICOLON': LeafRegexNode(ALPHABET['SEMICOLON']),
    'DOT': LeafRegexNode(ALPHABET['DOT']),
    'PLUS': LeafRegexNode(ALPHABET['PLUS']),
    'MINUS': LeafRegexNode(ALPHABET['MINUS']),
    'STAR' : LeafRegexNode(ALPHABET['STAR']),
    'ASSIGN': LeafRegexNode(ALPHABET['ASSIGN']),
    'EQUAL': BinaryRegexNode(LeafRegexNode(ALPHABET['ASSIGN']), LeafRegexNode(ALPHABET['ASSIGN']), BinaryOperationType.CONCATENATION),
    'SLASH': LeafRegexNode(ALPHABET['SLASH']),
    'STR': str_regex(),
    'BOOL': None,
    'KEYWORD': None
}


def dfa_for_scanner() -> DFA:
    auts = []
    for token, regex in TOKENS_REGEXPS.items():
        if regex is not None:
            nfa = RegexToNFA(regex)
            nfa.trap.make_terminal(token)
            auts.append(nfa)

    final_nfa = nfa_unite(auts)
    final_dfa = NFAToMFDFA(final_nfa)
    return final_dfa
