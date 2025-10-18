def optimize_intermediate(ir_code):
    optimized = []
    for line in ir_code:
        if line not in optimized:
            optimized.append(line)
    return optimized
