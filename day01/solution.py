from operator import mod

def part1(data):
    password = 0
    dial = 50
    for line in data.splitlines():
        rotation = transformRotation(line)
        dial = handleDial(dial, rotation)
        if dial == 0:
            password += 1

    return password

def transformRotation(rotation):
    direction = rotation[0]
    amount = int(rotation[1:])
    if direction == 'L':
        return -amount
    elif direction == 'R':
        return amount
    else:
        raise ValueError("Invalid rotation direction")

def handleDial(dial, change):
    return mod(dial + change, 100)

def part2(data):
    password = 0
    current_abs = 50
    for line in data.splitlines():
        change = transformRotation(line)
        next_abs = current_abs + change
        
        if change > 0:
            count = (next_abs // 100) - (current_abs // 100)
        else:
            count = ((current_abs - 1) // 100) - ((next_abs - 1) // 100)
            
        password += count
        current_abs = next_abs

    return password

with open("day01/input.txt") as f:
    data = f.read().strip()

print('part1:', part1(data))
print('part2:', part2(data))