def generate_machine_code(ir_code):
    machine = []
    lbl = 0
    for line in ir_code:
        if '=' in line:
            var, expr = line.split('=')
            machine.append(f"LOAD R1, {expr.strip()}")
            machine.append(f"STORE {var.strip()}, R1")
        elif line.startswith('PRINT'):
            val = line.replace('PRINT ', '').strip()
            machine.append(f"OUTPUT {val}")
        elif line.startswith('IF'):
            cond = line.replace('IF ', '').strip()
            lbl += 1
            machine.append(f"CMP {cond}")
            machine.append(f"JMP_FALSE ELSE_{lbl}")
        elif line == 'ELSE':
            machine.append(f"ELSE_{lbl}:")
    return machine
