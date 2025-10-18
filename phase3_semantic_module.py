class SemanticModule:
    def __init__(self, tokens):
        self.tokens = tokens
        self.symbol_table = {}

    def perform_semantic_analysis(self):
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]

            # ✅ Support for multiple data types
            if token[0] == 'KEYWORD' and token[1] in ('int', 'float', 'string', 'bool', 'char'):
                var_type = token[1]
                var_name = self.tokens[i + 1][1]  # next token is variable name

                # ❌ Check for redeclaration
                if var_name in self.symbol_table:
                    raise Exception(f"Semantic Error: Variable '{var_name}' redeclared.")

                var_value = None

                # ✅ Capture initialization (e.g., = value;)
                if i + 2 < len(self.tokens) and self.tokens[i + 2][1] == '=':
                    if i + 3 < len(self.tokens):
                        next_val = self.tokens[i + 3][1]

                        # 🧠 Handle string or char literals with quotes
                        if isinstance(next_val, str) and (next_val.startswith('"') or next_val.startswith("'")):
                            var_value = next_val.strip('"').strip("'")
                        # 🧠 Convert numeric literals to correct type
                        elif var_type == 'int':
                            try:
                                var_value = int(next_val)
                            except:
                                var_value = next_val
                        elif var_type == 'float':
                            try:
                                var_value = float(next_val)
                            except:
                                var_value = next_val
                        else:
                            var_value = next_val

                # ✅ Add to symbol table
                self.symbol_table[var_name] = {
                    'name': var_name,
                    'type': var_type,
                    'value': var_value,
                    'scope': 'global'
                }

            i += 1

        return self.symbol_table
