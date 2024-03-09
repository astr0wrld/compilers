from scanner_folder.classes import ALPHABET, TOKENS, get_token, Lexem, Table


class Scanner:
    def __init__(self, table: Table, keywords=None):
        self.table = table
        self.lexemes = []
        self.keywords = keywords if keywords is not None else []

    def traversal(self, text):
        
        is_correct = False
        value = ""
        cur_token = None
        cur_state = self.table.start
        num_of_read = 0

        for i in range(len(text)):
            if len(value) > 255:
                raise Exception("The variable name must be less than 255 characters")
            letter = text[i]
            if get_token(letter) not in self.table[cur_state].keys() or self.table[cur_state][get_token(letter)] == self.table.error:
                if not is_correct:
                    raise Exception(f"Language doesn't support {text}")
                if value in self.keywords:
                    self.lexemes.append(Lexem(TOKENS.KEYWORD.name, value))
                elif value in ['True', 'False']:
                    self.lexemes.append(Lexem(TOKENS.BOOL.name, value == 'True'))
                else:
                    self.lexemes.append(Lexem(cur_token[0], value))
                return text[i:]
            else:
                is_correct = True
                cur_state = self.table[cur_state][get_token(letter)]
                cur_token = list(cur_state.terminals)
                value += letter
                num_of_read += 1

        if len(cur_token) != 1:
                    print(cur_token)
                    raise Exception(f"Ambiguous lexeme for {text}")
        
        if len(value) < len(text):
            raise Exception(f"{text} is not a valid token")
        
        if value in self.keywords:
            self.lexemes.append(Lexem(TOKENS.KEYWORD.name, value))

        elif value in ['True', 'False']:
            self.lexemes.append(Lexem(TOKENS.BOOL.name, value == 'True'))

        else:
            self.lexemes.append(Lexem(cur_token[0], value))

        return text[num_of_read:]

    def scan_text(self, text: str):
        next_text = self.traversal(text)
        if next_text != '':
            self.scan_text(next_text)

    def scan(self, text: str):
        self.scan_text(text)
        lexemes = [str(lex) for lex in self.lexemes]
        self.lexemes = []
        return lexemes
