class ParserModule:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def consume(self, expected_type=None, expected_value=None):
        token = self.peek()
        if expected_type and token[0] != expected_type:
            raise Exception(f"Syntax Error: Expected {expected_type}, got {token}")
        if expected_value and token[1] != expected_value:
            raise Exception(f"Syntax Error: Expected '{expected_value}', got '{token[1]}'")
        self.pos += 1
        return token

    def parse(self):
        while self.pos < len(self.tokens) and self.peek()[0] != 'EOF':
            self.statement()
        return True

    def statement(self):
        token = self.peek()
        # ---------------- Variable Declaration ----------------
        if token[0] == 'KEYWORD' and token[1] in ('int', 'float', 'string', 'bool', 'char'):
            self.consume('KEYWORD')
            self.consume('IDENTIFIER')
            if self.peek()[1] == '=':
                self.consume('OPERATOR', '=')
                self.expression()
            self.consume('SEPARATOR', ';')
        # ---------------- Assignment ----------------
        elif token[0] == 'IDENTIFIER':
            self.consume('IDENTIFIER')
            self.consume('OPERATOR', '=')
            self.expression()
            self.consume('SEPARATOR', ';')
        # ---------------- Print ----------------
        elif token[0] == 'KEYWORD' and token[1] == 'print':
            self.consume('KEYWORD', 'print')
            self.consume('SEPARATOR', '(')
            self.expression()
            self.consume('SEPARATOR', ')')
            self.consume('SEPARATOR', ';')
        # ---------------- If-Else ----------------
        elif token[0] == 'KEYWORD' and token[1] == 'if':
            self.if_else_block()
        # ---------------- While Loop ----------------
        elif token[0] == 'KEYWORD' and token[1] == 'while':
            self.consume('KEYWORD', 'while')
            self.consume('SEPARATOR', '(')
            self.expression()
            self.consume('SEPARATOR', ')')
            self.consume('SEPARATOR', '{')
            while self.peek()[1] != '}':
                self.statement()
            self.consume('SEPARATOR', '}')
        # ---------------- Closing brace ----------------
        elif token[1] == '}':
            return
        else:
            raise Exception(f"Syntax Error: Unexpected token {token}")

    # ---------------- If-Else Block ----------------
    def if_else_block(self):
        self.consume('KEYWORD', 'if')
        self.consume('SEPARATOR', '(')
        self.expression()
        self.consume('SEPARATOR', ')')
        self.consume('SEPARATOR', '{')
        while self.peek()[1] not in ('}', 'EOF'):
            self.statement()
        self.consume('SEPARATOR', '}')
        if self.peek()[0] == 'KEYWORD' and self.peek()[1] == 'else':
            self.consume('KEYWORD', 'else')
            self.consume('SEPARATOR', '{')
            while self.peek()[1] not in ('}', 'EOF'):
                self.statement()
            self.consume('SEPARATOR', '}')

    # ---------------- Expression Parsing ----------------
    def expression(self):
        while self.peek()[1] not in (';', ')', '{', '}', 'EOF'):
            token = self.peek()
            # Allow identifiers, numbers, string literals, char literals, booleans, operators
            if token[0] in ('IDENTIFIER', 'NUMBER', 'STRING_LITERAL', 'CHAR_LITERAL'):
                self.consume()
            elif token[0] == 'KEYWORD' and token[1] in ('true', 'false'):
                self.consume()
            elif token[0] == 'OPERATOR':
                self.consume()
            elif token[0] == 'SEPARATOR' and token[1] in ('(', ')'):
                self.consume()
            else:
                break
