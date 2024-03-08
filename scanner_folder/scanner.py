from scanner_folder.classes import ALPHABET, TOKENS, get_token, Lexem, Table

def split(text: str, delimeters=' \t\n'):
    result = []
    current = ''
    for char in text:
        if char not in delimeters:
            current += char
        elif current:
            result.append(current)
            current = ''
        
    if current:
        result.append(current)

    return result     


class Scanner:
    def __init__(self, table: Table, keywords=None):
        self.table = table
        self.lexemes = []
        self.keywords = keywords if keywords is not None else []

    def traversal(self, word):
        if len(word) > 255:
            raise Exception("The variable name must be less than 255 characters")

        value = ""
        cur_token = None
        cur_state = self.table.start

        for i in range(len(word)):
            letter = word[i]
            if get_token(letter) not in self.table[cur_state].keys() or self.table[cur_state][get_token(letter)] == self.table.error:
                if value == "":
                    raise Exception(f"Language doesn't support {word}")
                self.lexemes.append(Lexem(cur_token[0], value))
                return word[i:]
            else:
                cur_state = self.table[cur_state][get_token(letter)]
                cur_token = list(cur_state.terminals)
                value += letter

        if len(cur_token) != 1:
                    print(cur_token)
                    raise Exception(f"Ambiguous lexeme for {word}")
        
        if len(value) < len(word):
            raise Exception(f"{word} is not a valid token")

        self.lexemes.append(Lexem(cur_token[0], value))

    def read_num(self, word: str):
        num = 0
        for i in range(len(word)):
            if word[i] in ALPHABET['NUM']:
                num = num * 10 + int(word[i])
            else:
                self.lexemes.append(Lexem(TOKENS.NUM.name, num))
                return word[i:]
        self.lexemes.append(Lexem(TOKENS.NUM.name, num))

    def read_bool(self, word: str):
            self.lexemes.append(Lexem(TOKENS.BOOL.name, word == 'true'))

    def read_string(self, word: str):
        self.lexemes.append(Lexem(TOKENS.STR.name, word[1:-1]))

    def scan_word(self, word: str):
        if word[0] == ' ':
            pass
        
        elif word[0] == '0':
            raise Exception('Zero cannot be the first character')
        
        elif word[0] in ALPHABET['NUM']:
            next_word = self.read_num(word)
            if next_word is not None:
                self.scan_word(next_word)

        elif word in ['true', 'false']:
                self.read_bool(word)

        elif word[0] == ALPHABET['QUOTE']:
            if word[-1] != ALPHABET['QUOTE']:
                raise Exception('No closing quote detected')
            self.read_string(word)

        elif word in self.keywords:
            self.lexemes.append(Lexem(TOKENS.KEYWORD.name, word))

        else:
            next_word = self.traversal(word)
            if next_word is not None:
                self.scan_word(next_word)
    
    def scan(self, text: str):
        words = split(text)
        words = [word for word in words if word is not None and word != '']
        for i in range(len(words)):
            self.scan_word(words[i])

        lexemes = [str(lex) for lex in self.lexemes]
        self.lexemes = []
        return lexemes
