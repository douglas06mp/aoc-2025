def part1(data):
    first = data.splitlines()[0]
    length = len(first)
    beams = [0] * length

    start = first.index("S")
    beams[start] = 1
    splitTimes = 0

    for line in data.splitlines()[1:]:
        newBeams = [0] * length
        for i in range(length):
            if beams[i] > 0:
                if line[i] == "^":
                    if i > 0:
                        newBeams[i - 1] = beams[i]
                    if i < length - 1:
                        newBeams[i + 1] = beams[i]

                    splitTimes += 1
                else:
                    newBeams[i] = beams[i]

        beams = newBeams

    return splitTimes

def part2(data):
    first = data.splitlines()[0]
    length = len(first)
    beams = [0] * length

    start = first.index("S")
    beams[start] = 1
    dp = [0] * length
    dp[start] = 1

    for line in data.splitlines()[1:]:
        newBeams = [0] * length
        for i in range(length):
            if beams[i] > 0:
                if line[i] == "^":
                    if i > 0:
                        newBeams[i - 1] = beams[i]
                        dp[i - 1] += dp[i]
                    if i < length - 1:
                        newBeams[i + 1] = beams[i]
                        dp[i + 1] += dp[i]

                    dp[i] = 0
                else:
                    newBeams[i] = beams[i]

        beams = newBeams

    return sum(dp)


with open("day07/input.txt") as f:
    data = f.read().strip()

print("part 1: ", part1(data))
print("part 2: ", part2(data))
