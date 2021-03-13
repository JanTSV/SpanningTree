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
        # Scan the source
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.add_token(TokenType.EOF)
        if self.had_error:
            self.tokens = []
        return self.tokens

    def scan_token(self):
        # Add the specific tokens to the tokens array
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
        # Read the text until the is no digit and add it to the tokens
        while self.is_digit(self.peek()):
            self.advance()
        text = self.source[self.start:self.current]
        self.add_token(TokenType.NUMBER, int(text))

    def is_digit(self, c):
        # Check if a char is a digit
        c = ord(c)
        return (c >= ord('0')) and (c <= ord('9'))

    def identifier(self):
        # Read the identifier of the node and add it to the tokens
        while self.is_alpha(self.peek()):
            self.advance()
        text = self.source[self.start:self.current]
        self.add_token(TokenType.IDENTIFIER, text)

    def add_token(self, x, literal=None):
        # Add a token x with value literal to the tokens array
        text = self.source[self.start:self.current]
        self.tokens.append(Token(x, text, literal, self.line))

    def is_alpha(self, c):
        # Check if a char is a letter or an underscore
        c = ord(c)
        return ((c >= ord('a')) and (c <= ord('z'))) or ((c >= ord('A')) and (c <= ord('Z'))) or (c == ord('_'))

    def advance(self):
        # Advance the current read position
        self.current += 1
        return self.source[self.current - 1]

    def is_at_end(self):
        # Check if current reached the end of the source
        return self.current >= len(self.source)
    
    def peek(self):
        # L(1)
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def error(self, message, details=[]):
        # Print error to console
        self.had_error = True
        print(F"Scanner: ERROR <line: {self.line} character: {self.current-1}>\t{message}")
        if len(details) > 0:
            s = "DETAILS: "
            for v in details:
                s += F"'{v}' "
            print(s)
