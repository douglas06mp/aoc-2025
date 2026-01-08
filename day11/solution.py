def part1(data):
    graph = {}

    for line in data.strip().splitlines():
        fromNode = line.split(":")[0]
        toNodes = line.split(":")[1].strip().split()
        graph[fromNode] = toNodes

    pathCount = 0

    def dfs(node):
        nonlocal pathCount
        if node == "out":
            pathCount += 1
            return
        for neighbor in graph.get(node, []):
            dfs(neighbor)

    dfs("you")

    return pathCount


def part2(data):
    graph = {}

    for line in data.strip().splitlines():
        fromNode = line.split(":")[0]
        toNodes = line.split(":")[1].strip().split()
        graph[fromNode] = toNodes

    # cache: key = (node, seenDAC, seenFFT), value = pathCount
    cache = {}

    def dfs(node, seenDAC=False, seenFFT=False) -> int:
        # Check if result is already cached
        key = (node, seenDAC, seenFFT)
        if key in cache:
            return cache[key]
        
        pathCount = 0

        for neighbor in graph.get(node, []):
            newSeenDAC = seenDAC or neighbor == "dac"
            newSeenFFT = seenFFT or neighbor == "fft"

            if neighbor == "out":
                if newSeenFFT and newSeenDAC:
                    pathCount += 1
                continue

            pathCount += dfs(neighbor, newSeenDAC, newSeenFFT)
        
        # Store result in cache before returning
        cache[key] = pathCount
        return pathCount

    return dfs("svr")

with open("day11/input.txt") as f:
    data = f.read().strip()

print("part 1: ", part1(data))
print("part 2: ", part2(data))
