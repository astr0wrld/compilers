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


TOKENS_REGEXPS = {
    'VARNAME': var_regex(),
    'NUM': None,
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
    'STR': None,
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
