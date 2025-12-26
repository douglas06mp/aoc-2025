from collections import Counter

def part1(data):
    coords = []
    for line in data.splitlines():
        coord = tuple(int(s) for s in line.split(','))
        coords.append(coord)

    # Calculate all pairwise distances, [(coord1, coord2, distance)]
    distances = []
    for i, coord in enumerate(coords):
        for j in range(i + 1, len(coords)):
            coord2 = coords[j]
            dist = (coord[0] - coord2[0]) ** 2 + (coord[1] - coord2[1]) ** 2 + (coord[2] - coord2[2]) ** 2
            distances.append((coord, coord2, dist))

    # Sort distances
    sortedDistances = sorted(distances, key=lambda x: x[2])

    # Union-Find to group coordinates
    parents = {coord: coord for coord in coords}

    # Find with path compression
    def find(coord):
        if parents[coord] != coord:
            parents[coord] = find(parents[coord])
        return parents[coord]
    
    # Union operation
    def union(coord1, coord2):
        root1 = find(coord1)
        root2 = find(coord2)
        if root1 != root2:
            parents[root1] = root2

    for coord1, coord2, dist in sortedDistances[:1000]:
        union(coord1, coord2)

    roots = [find(coord) for coord in coords]
    sortedRoots = sorted(Counter(roots).values(), reverse=True)

    return sortedRoots[0] * sortedRoots[1] * sortedRoots[2]

def part2(data):
    return 0

with open("day08/input.txt") as f:
    data = f.read().strip()

print("part 1: ", part1(data))
print("part 2: ", part2(data))
