from enum import Enum

from automatons.classes import DFA


ALPHABET = {
    'SPACE': ' \n\t',
    'STR': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'NUM': '0123456789',
    'L_FIGURE_BR': '{',
    'R_FIGURE_BR': '}',
    'L_ROUND_BR': '(',
    'R_ROUND_BR': ')',
    'QUOTE': '"',
    'SEMICOLON': ';',
    'DOT': '.',
    'PLUS': '+',
    'MINUS': '-',
    'STAR' : '*',
    'ASSIGN': '=',
    'EQUAL': '==',
    'SLASH': '/'
}

KEYWORDS = [
    'fun',
    'if',
    'else',
    'for',
    'while'
]

class TOKENS(Enum):
    SPACE = 'SPACE'
    VARNAME = 'VARNAME'
    NUM = 'NUM'
    L_FIGURE_BR = 'L_FIGURE_BR'
    R_FIGURE_BR = 'R_FIGURE_BR'
    L_ROUND_BR = 'L_ROUND_BR'
    R_ROUND_BR = 'R_ROUND_BR'
    QUOTE = 'QUOTE'
    SEMICOLON = 'SEMICOLON'
    DOT = 'DOT'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    STAR = 'STAR'
    ASSIGN = 'ASSIGN'
    EQUAL = 'EQUAL'
    SLASH = 'SLASH'
    STR = 'STR'
    BOOL = 'BOOL'
    KEYWORD = 'KEYWORD'


class Lexem:
    def __init__(self, token, value=None) -> None:
        self.token = token
        self.value = value

    def __str__(self):
        return f"{self.token}({self.value})"
    

def get_token(letter: str):
    for token, text in ALPHABET.items():
        if letter in text:
            return token


class Table:
    def __init__(self, dfa: DFA) -> None:
        self.table = {}
        self.fill_table(dfa)

    def __getitem__(self, state):
        return self.table[state]
    
    def fill_table(self, dfa: DFA):
        for state in dfa.states:
            if state == dfa.root:
                self.start = state
            elif state == dfa.trap:
                self.error = dfa.trap

            self.table[state] = dict()
            for letter in dfa.alphabet:
                self.table[state][get_token(letter)] = state.transitions[letter]

