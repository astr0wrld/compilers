from scanner_folder.dfa_for_scanner import dfa_for_scanner
from scanner_folder.classes import KEYWORDS, Table
from scanner_folder.scanner import Scanner


def test_scanner():
    keywords = KEYWORDS
    lang_alphabet_dfa = dfa_for_scanner()
    table = Table(lang_alphabet_dfa)
    scanner = Scanner(table, keywords)

    with open('scanner_input.txt', 'r') as input:
        print("\n--------------\n", end='')
        for line in input:
            scanned = scanner.scan(line)
            print(line)
            print()
            print(scanned, end='')
            print("\n--------------\n", end='')

test_scanner()