from TokenType import TokenType


class Token:
    def __init__(self, t, lexeme: str, literal, line: int):
        self.t = t
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return F"<line: {self.line}, type: {self.t.name} | {self.lexeme} {self.literal}>"