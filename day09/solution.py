def part1(data):
    maxArea = 0
    coords = [tuple(map(int, line.split(','))) for line in data.splitlines()]

    for i in range(len(coords)):
        x, y = coords[i]
        for j in range(i+1, len(coords)):
            x2, y2 = coords[j]
            area = (abs(x - x2) + 1) * (abs(y - y2) + 1)
            if area > maxArea:
                maxArea = area
        
    return maxArea

def part2(data):
    return 0

with open('day09/input.txt') as f:
    data = f.read().strip()

print("part 1: ", part1(data))
print("part 2: ", part2(data))