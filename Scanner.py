from TokenType import TokenType
from Token import Token

class Scanner:
    def __init__(self, source):
        self.source = source
        self.current = 0
        self.start = self.current
        self.had_error = False
        self.line = 1
        self.tokens = []

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.add_token(TokenType.EOF)
        if self.had_error:
            self.tokens = []
        return self.tokens

    def scan_token(self):
        c = self.advance()
        if c == ';':
            self.add_token(TokenType.SEMICOLON)
        elif c == '=':
            self.add_token(TokenType.EQUAL)
        elif c == ':':
            self.add_token(TokenType.COLON)
        elif c == '-':
            self.add_token(TokenType.MINUS)
        elif c == ' ' or c == '\t' or c == '\r':
            pass
        elif c == '/' and self.peek() == '/':
            while (self.peek() != '\n') and (not self.is_at_end()):
                self.advance()
        elif c == '\n':
            self.line += 1
        else:
            if self.is_alpha(c):
                self.identifier()
            elif self.is_digit(c):
                self.number()
            else:
                self.error("Unexpected token.", [self.source[self.current - 1]])

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()
        text = self.source[self.start:self.current]
        self.add_token(TokenType.NUMBER, int(text))

    def is_digit(self, c):
        c = ord(c)
        return (c >= ord('0')) and (c <= ord('9'))

    def identifier(self):
        while self.is_alpha(self.peek()):
            self.advance()
        text = self.source[self.start:self.current]
        self.add_token(TokenType.IDENTIFIER, text)

    def add_token(self, x, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(x, text, literal, self.line))

    def is_alpha(self, c):
        c = ord(c)
        return ((c >= ord('a')) and (c <= ord('z'))) or ((c >= ord('A')) and (c <= ord('Z'))) or (c == ord('_'))

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def is_at_end(self):
        return self.current >= len(self.source)
    
    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def error(self, message, details=[]):
        self.had_error = True
        print(F"Scanner: ERROR <line: {self.line} character: {self.current-1}>\t{message}")
        if len(details) > 0:
            s = "DETAILS: "
            for v in details:
                s += F"'{v}' "
            print(s)
