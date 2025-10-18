def generate_final_assembly(machine_code):
    asm = []
    asm.append("section .text")
    asm.append("global _start")
    asm.append("_start:")
    for line in machine_code:
        asm.append(line)
    asm.append("mov eax, 1")
    asm.append("mov ebx, 0")
    asm.append("int 0x80")
    return asm
