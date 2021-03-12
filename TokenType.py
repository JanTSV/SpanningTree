from enum import Enum

class TokenType(Enum):
    # Single character tokens
    EQUAL = 0
    SEMICOLON = 1
    MINUS = 2
    COLON = 3

    # Literals
    IDENTIFIER = 4
    NUMBER = 5

    EOF = 6
