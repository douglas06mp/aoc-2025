def part1(data):
    maxX = len(data.splitlines()[0])
    maxY = len(data.splitlines())
    count = 0

    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            if char == '@' and isAccesible(data.splitlines(), x, y, maxX, maxY):
                count += 1

    return count

def isAccesible(grid, x, y, maxX, maxY):
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

    paperCount = 0
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if isValidGridPos(nx, ny, maxX, maxY) and grid[ny][nx] == '@':
            paperCount += 1

    return paperCount <= 3


def isValidGridPos(x, y, maxX, maxY):
    return x >= 0 and x < maxX and y >= 0 and y < maxY

def part2(data):
    maxX = len(data.splitlines()[0])
    maxY = len(data.splitlines())
    count = 0
    removedPapers = set()

    while True:
        for y, line in enumerate(data.splitlines()):
            for x, char in enumerate(line):
                if char == '@' and isAccesible(data.splitlines(), x, y, maxX, maxY):
                    removedPapers.add((x, y))
                    count += 1

        if len(removedPapers) == 0:
            break

        newGrid = []
        for y, line in enumerate(data.splitlines()):
            newLine = ''
            for x, char in enumerate(line):
                if (x, y) in removedPapers:
                    newLine += '.'
                else:
                    newLine += char
            newGrid.append(newLine)

        data = '\n'.join(newGrid)
        removedPapers.clear()

    return count


with open("day04/input.txt") as f:
    data = f.read().strip()

print('part1:', part1(data))
print('part2:', part2(data))