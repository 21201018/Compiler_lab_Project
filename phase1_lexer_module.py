import re

def perform_lexical_analysis(code):
    token_patterns = [
        # ✅ Keywords
        ('KEYWORD', r'\b(int|float|string|bool|char|if|else|while|print)\b'),

        # ✅ String literals (double quotes)
        ('STRING_LITERAL', r'"[^"]*"'),

        # ✅ Char literals (single quotes)
        ('CHAR_LITERAL', r"'[^']'"),

        # ✅ Identifiers
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),

        # ✅ Numbers (int or float)
        ('NUMBER', r'\d+(\.\d+)?'),

        # ✅ Operators
        ('OPERATOR', r'[+\-*/=<>!&]'),

        # ✅ Separators
        ('SEPARATOR', r'[(){};,]'),

        # ✅ Whitespace (skip)
        ('WHITESPACE', r'\s+'),
    ]

    tokens = []

    while code:
        match = None
        for token_type, pattern in token_patterns:
            regex = re.match(pattern, code)
            if regex:
                match = regex.group(0)
                if token_type != 'WHITESPACE':
                    # ✅ Strip quotes for string/char if desired
                    if token_type == 'STRING_LITERAL':
                        match = match  # keep quotes for semantic module or strip later
                    elif token_type == 'CHAR_LITERAL':
                        match = match
                    tokens.append((token_type, match))
                code = code[len(match):]
                break
        if not match:
            raise Exception(f"Lexical Error near '{code[0]}'")
    return tokens
