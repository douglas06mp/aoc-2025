import re
from itertools import combinations

def parse_machine(line):
    # Parse the indicator lights pattern [.##.]
    lights_match = re.search(r"\[([.#]+)\]", line)
    lights = lights_match.group(1)
    target = ""
    for c in lights:
        target += "1" if c == "#" else "0"

    # Parse button wiring schematics (3) (1,3) (2) etc.
    buttons = []
    button_matches = re.findall(r"\(([0-9,]+)\)", line)
    for button_str in button_matches:
        indices = [int(x) for x in button_str.split(",")]
        buttons.append(indices)

    # Parse joltage requirements {3,5,4,7}
    joltage_match = re.search(r"\{([0-9,]+)\}", line)
    joltage = [int(x) for x in joltage_match.group(1).split(",")]

    return target, buttons, joltage

def solve_machine(target, buttons):
    # Convert buttons to binary masks for XOR operations
    n_lights = len(target)
    button_masks = []
    for indices in buttons:
        mask = [0] * n_lights
        for idx in indices:
            if idx < n_lights:
                mask[idx] = 1
        button_masks.append("".join(str(x) for x in mask))
    
    target_int = int(target, 2)
    for buttonLength in range(1, len(button_masks) + 1):
        # Loop through all combinations of buttons of length buttonLength
        for combo in combinations(button_masks, buttonLength):
            result = 0
            for button in combo:
                result ^= int(button, 2)
            if result == target_int:
                return buttonLength

    return 0

def part1(data):
    total = 0
    for line in data.strip().splitlines():
        target, buttons, joltage = parse_machine(line)
        presses = solve_machine(target, buttons)
        total += presses

    return total

def solve_joltage(buttons, joltage):
    """
    Solve the joltage problem using Integer Linear Programming.
    Find minimum total button presses such that each counter reaches its target.
    
    This is: minimize sum(x_i) 
    subject to: A * x = joltage, x >= 0, x integer
    where A[j][i] = 1 if button i affects counter j
    """
    from scipy.optimize import milp, LinearConstraint, Bounds
    import numpy as np
    
    n_buttons = len(buttons)
    n_counters = len(joltage)
    
    # Build coefficient matrix: A[counter][button] = 1 if button affects counter
    A = np.zeros((n_counters, n_buttons))
    for i, button_indices in enumerate(buttons):
        for counter_idx in button_indices:
            if counter_idx < n_counters:
                A[counter_idx][i] = 1
    
    # Objective: minimize sum of all button presses
    c = np.ones(n_buttons)
    
    # Constraints: A * x = joltage (equality)
    constraints = LinearConstraint(A, joltage, joltage)
    
    # Bounds: x >= 0, integers
    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(n_buttons)  # All variables are integers
    
    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    if result.success:
        return int(round(result.fun))
    else:
        return -1

def part2(data):
    total = 0
    for line in data.strip().splitlines():
        target, buttons, joltage = parse_machine(line)
        presses = solve_joltage(buttons, joltage)
        if presses == -1:
            return -1
        total += presses

    return total

with open("day10/input.txt") as f:
    data = f.read().strip()

print("part 1: ", part1(data))
print("part 2: ", part2(data))
