from phase1_lexer_module import perform_lexical_analysis
from phase2_parser_module import ParserModule
from phase3_semantic_module import SemanticModule
from phase4_ir_module import IRModule
from phase5_optimizer_module import optimize_intermediate
from phase6_codegen_module import generate_machine_code
from phase7_assembly_module import generate_final_assembly

# ===========================================================
# 🧠 REALISTIC COMBINED SOURCE PROGRAM (MULTI-TYPE SUPPORT)
# ===========================================================
program_code = """
int students = 20;
float marks = 88.5;
string name = "Alice";
bool isPassed = true;
char grade = 'A';

int books_per_student = 3;
int total_books;
total_books = students * books_per_student + 5;
print(total_books);

int days = 7;
int hours_per_day = 6;
int total_hours;
total_hours = days * hours_per_day;
print(total_hours);

int level = 1;
int target = 3;
while (level <= target) {
    print(level);
    level = level + 1;
}
print(level);

float temp_today = 32.5;
float temp_yesterday = 29.7;
if (temp_today > temp_yesterday) {
    print(temp_today);
} else {
    print(temp_yesterday);
}

int units_used = 75;
int cost_per_unit = 6;
int bill_amount;
bill_amount = units_used * cost_per_unit;
print(bill_amount);

int tank_capacity = 200;
int water_used = 50;
int water_left;
water_left = tank_capacity - water_used;
print(water_left);

if (bill_amount > 400 && water_left < 100) {
    print(bill_amount);
    print(water_left);
} else {
    print(total_books);
    print(total_hours);
}
"""

# ===========================================================
#              MINI COMPILER EXECUTION PIPELINE
# ===========================================================
print("=================================================")
print("      MINI COMPILER PROJECT - FINAL EDITION   ")
print("=================================================")

try:
    # ------------------ PHASE 1 ------------------
    print("\n[PHASE 1] Lexical Analysis")
    tokens = perform_lexical_analysis(program_code)
    for t in tokens:
        print(t)

    # ------------------ PHASE 2 ------------------
    print("\n[PHASE 2] Syntax Analysis")
    parser = ParserModule(tokens)
    parser.parse()
    print("✔ Syntax check passed successfully.")

    # ------------------ PHASE 3 ------------------
    print("\n[PHASE 3] Semantic Analysis")
    sem = SemanticModule(tokens)
    symbols = sem.perform_semantic_analysis()

    print("✔ Symbol Table:")
    print("-------------------------------------------------------------")
    print(f"{'Name':<15} | {'Type':<10} | {'Value':<15} | {'Scope'}")
    print("-------------------------------------------------------------")

    # ✅ FIXED PRINTING LOGIC — Works for multi-type data
    for name, info in symbols.items():
        if isinstance(info, dict):
            print(f"{info.get('name', name):<15} | "
                  f"{info.get('type', ''):<10} | "
                  f"{str(info.get('value', '')):<15} | "
                  f"{info.get('scope', '')}")
        else:
            print(f"{name:<15} | {str(info):<10} | {'-':<15} | global")

    print("-------------------------------------------------------------")

    # ------------------ PHASE 4 ------------------
    print("\n[PHASE 4] Intermediate Code Generation")
    ir = IRModule(tokens)
    icode = ir.generate_ir()
    for line in icode:
        print(line)

    # ------------------ PHASE 5 ------------------
    print("\n[PHASE 5] Optimization")
    optimized = optimize_intermediate(icode)
    for line in optimized:
        print(line)

    # ------------------ PHASE 6 ------------------
    print("\n[PHASE 6] Target Code Generation")
    machine = generate_machine_code(optimized)
    for line in machine:
        print(line)

    # ------------------ PHASE 7 ------------------
    print("\n[PHASE 7] Final Assembly Output")
    assembly = generate_final_assembly(machine)
    for line in assembly:
        print(line)

    print("\n✔ Compilation Finished Successfully!")

except Exception as e:
    print(f"\n❌ Error during compilation: {e}")
