def part1(data):
    patterns = {}
    count = 0

    for line in data.strip().splitlines():
        if line.endswith(":"):
            key = int(line.split(":")[0])
            patterns[key] = 0
            continue
        elif "#" in line:
            patterns[key] += line.count("#")
            continue
        elif "x" in line:
            widthAndLength = line.split(":")[0]
            width, length = map(int, widthAndLength.split("x"))
            area = width * length

            quantities = [int(x) for x in line.split(":")[1].strip().split()]
            areaOfPatterns = sum(patterns[idx] * q for idx, q in enumerate(quantities))
            if areaOfPatterns <= area:
                count += 1

    return count


def part2(data):
    return 0


with open("day12/input.txt") as f:
    data = f.read().strip()

print("part 1: ", part1(data))
print("part 2: ", part2(data))
