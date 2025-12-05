def part1(idRanges, ingredientIds):
    count = 0
    fn = lambda x: any(s <= x <= e for s, e in idRanges)

    for ingredientId in ingredientIds:
        if fn(ingredientId):
            count += 1

    return count


def part2(idRanges):
    mergedRanges = []
    sortedRanges = sorted(idRanges, key=lambda x: x[0])

    for range in sortedRanges:
        if not mergedRanges or mergedRanges[-1][1] < range[0]:
            mergedRanges.append(range)
        else:
            mergedRanges[-1] = (mergedRanges[-1][0], max(mergedRanges[-1][1], range[1]))

    count = 0
    for start, end in mergedRanges:
        count += end - start + 1

    return count


with open("day05/input.txt") as f:
    idRanges = []
    ingredientIds = []
    data = f.read().strip()
    for line in data.splitlines():
        if "-" in line:
            start, end = map(int, line.split("-"))
            idRanges.append((start, end))
        elif line.isdigit():
            ingredientIds.append(int(line))


print("part1: ", part1(idRanges, ingredientIds))
print("part2: ", part2(idRanges))
