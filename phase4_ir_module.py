class IRModule:
    def __init__(self, tokens):
        self.tokens = tokens
        self.ir = []

    def generate_ir(self):
        for i, t in enumerate(self.tokens):
            if t[1] == '=':
                lhs = self.tokens[i-1][1]
                rhs = ''
                j = i+1
                while j < len(self.tokens) and self.tokens[j][1] != ';':
                    rhs += self.tokens[j][1] + ' '
                    j += 1
                self.ir.append(f"{lhs} = {rhs.strip()}")
            elif t[1] == 'print':
                self.ir.append(f"PRINT {self.tokens[i+2][1]}")
            elif t[1] == 'if':
                cond = self.tokens[i+2][1] + ' ' + self.tokens[i+3][1] + ' ' + self.tokens[i+4][1]
                self.ir.append(f"IF {cond}")
            elif t[1] == 'else':
                self.ir.append("ELSE")
        return self.ir
