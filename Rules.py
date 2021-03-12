from TokenType import TokenType


class Rules:
    def __init__(self):
        self.DECLARATION_RULE = {
            -2: {"expected": TokenType.IDENTIFIER, "error": "Expected identifier."},
             0: {"expected": TokenType.NUMBER, "error": "Expected value."},
             1: {"expected": TokenType.SEMICOLON, "error": "Expected semicolon."}
        }

        self.EDGE_RULE = {
            -2: {"expected": TokenType.IDENTIFIER, "error": "Expected left identifier."},
             0: {"expected": TokenType.IDENTIFIER, "error": "Expected right identifier."},
             1: {"expected": TokenType.COLON, "error": "Expected colon."},
             2: {"expected": TokenType.NUMBER, "error": "Expected value."},
             3: {"expected": TokenType.SEMICOLON, "error": "Expected semicolon."}
        }
