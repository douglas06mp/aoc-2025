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
        mask = [0] * len(target)
        for idx in button_str.split(","):
            mask[int(idx)] = 1
        buttons.append("".join(str(x) for x in mask))

    return target, buttons

def solve_machine(target, buttons):
    # target: 6 from '0110'
    # buttons: ['1000', '0101', '0010']
    for buttonLength in range(1, len(buttons) + 1):
        # Loop through all combinations of buttons of length buttonLength
        for combo in combinations(buttons, buttonLength):
            result = 0
            for button in combo:
                result ^= int(button, 2)
            if result == target:
                return buttonLength

    return 0

def part1(data):
    total = 0
    for line in data.strip().splitlines():
        target, buttons = parse_machine(line)
        presses = solve_machine(int(target, 2), buttons)
        total += presses

    return total

def part2(data):
    return 0

with open("day10/input.txt") as f:
    data = f.read().strip()

print("part 1: ", part1(data))
print("part 2: ", part2(data))
