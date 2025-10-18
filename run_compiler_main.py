from phase1_lexer_module import perform_lexical_analysis
from phase2_parser_module import ParserModule
from phase3_semantic_module import SemanticModule
from phase4_ir_module import IRModule
from phase5_optimizer_module import optimize_intermediate
from phase6_codegen_module import generate_machine_code
from phase7_assembly_module import generate_final_assembly

program_code = """
int num1 = 8;
int num2 = 12;
int result;
result = num1 + num2 - 3;
print(result);
if (result > 10) {
    print(result);
} else {
    print(num1);
}
"""

print("=================================================")
print("    MINI COMPILER PROJECT - CLASSMATE EDITION   ")
print("=================================================")

print("\n[PHASE 1] Lexical Analysis")
tokens = perform_lexical_analysis(program_code)
for t in tokens:
    print(t)

print("\n[PHASE 2] Syntax Analysis")
parser = ParserModule(tokens)
parser.parse()
print("✔ Syntax check passed successfully.")

print("\n[PHASE 3] Semantic Analysis")
sem = SemanticModule(tokens)
symbols = sem.perform_semantic_analysis()
print("✔ Symbol Table:", symbols)

print("\n[PHASE 4] Intermediate Code Generation")
ir = IRModule(tokens)
icode = ir.generate_ir()
for line in icode:
    print(line)

print("\n[PHASE 5] Optimization")
optimized = optimize_intermediate(icode)
for line in optimized:
    print(line)

print("\n[PHASE 6] Target Code Generation")
machine = generate_machine_code(optimized)
for line in machine:
    print(line)

print("\n[PHASE 7] Final Assembly Output")
assembly = generate_final_assembly(machine)
for line in assembly:
    print(line)

print("\n✔ Compilation Finished Successfully!")
