def part1(data):
    sum = 0
    n = 2
    for line in data.splitlines():
        lineSum = getLineSum(line, n)
        sum += lineSum

    return sum

def part2(data):
    sum = 0
    n = 12
    for line in data.splitlines():
        lineSum = getLineSum(line, n)
        sum += lineSum

    return sum

def getLineSum(str, n):
    lineSum = 0
    num = 0
    startIdx = 0

    while num < n:
        endIdx = len(str) - (n - num) + 1
        max, pos = findMaxAndPositionBetweenIdx(str, startIdx, endIdx)
        num += 1
        startIdx = startIdx + pos + 1
        lineSum += max * 10**(n - num)

    return lineSum

def findMaxAndPositionBetweenIdx(str, startIdx, endIdx):
    max = -1
    position = -1
    for i, ch in enumerate(str[startIdx:endIdx]):
        val = int(ch)
        if val > max:
            max = val
            position = i

    return max, position


with open("day03/input.txt") as f:
    data = f.read().strip()

print('part1:', part1(data))
print('part2:', part2(data))