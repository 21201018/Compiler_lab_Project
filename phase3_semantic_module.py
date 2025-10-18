class SemanticModule:
    def __init__(self, tokens):
        self.tokens = tokens
        self.symbol_table = {}

    def perform_semantic_analysis(self):
        for i, token in enumerate(self.tokens):
            if token[0] == 'KEYWORD' and token[1] in ('int', 'float'):
                variable = self.tokens[i+1][1]
                if variable in self.symbol_table:
                    raise Exception(f"Semantic Error: '{variable}' redeclared.")
                self.symbol_table[variable] = token[1]
        return self.symbol_table
