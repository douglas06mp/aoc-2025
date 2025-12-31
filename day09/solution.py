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
    coords = [tuple(map(int, line.split(','))) for line in data.splitlines()]
    n = len(coords)
    
    # Build edges
    edges = []
    for i in range(n):
        p1 = coords[i]
        p2 = coords[(i + 1) % n]
        edges.append((p1, p2))
    
    # Separate edges into vertical and horizontal for optimization
    v_edges = []
    h_edges = []
    for p1, p2 in edges:
        if p1[0] == p2[0]: # Vertical
            y_min, y_max = sorted((p1[1], p2[1]))
            v_edges.append((p1[0], y_min, y_max))
        else: # Horizontal
            x_min, x_max = sorted((p1[0], p2[0]))
            h_edges.append((p1[1], x_min, x_max))
            
    # Sort for potential binary search or just structured access
    v_edges.sort()
    h_edges.sort()

    def is_point_on_segment(px, py, p1, p2):
        if p1[0] == p2[0] == px: # Vertical
            return min(p1[1], p2[1]) <= py <= max(p1[1], p2[1])
        if p1[1] == p2[1] == py: # Horizontal
            return min(p1[0], p2[0]) <= px <= max(p1[0], p2[0])
        return False

    def is_point_in_polygon(px, py):
        # Check if on boundary first
        for p1, p2 in edges:
            if is_point_on_segment(px, py, p1, p2):
                return True
        
        # Ray casting to the right
        intersections = 0
        for x, y_min, y_max in v_edges:
            if x > px:
                if y_min <= py < y_max:
                    intersections += 1
        
        return intersections % 2 == 1

    def rect_intersects_edges(min_x, max_x, min_y, max_y):
        # Check vertical edges
        for x, edge_y_min, edge_y_max in v_edges:
            if min_x < x < max_x:
                # Check interval overlap (y_min, y_max) with (min_y, max_y)
                if max(min_y, edge_y_min) < min(max_y, edge_y_max):
                    return True
        
        # Check horizontal edges
        for y, edge_x_min, edge_x_max in h_edges:
            if min_y < y < max_y:
                # Check interval overlap (x_min, x_max) with (min_x, max_x)
                if max(min_x, edge_x_min) < min(max_x, edge_x_max):
                    return True
        return False

    # Generate all pairs and sort by area
    candidates = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = coords[i]
            p2 = coords[j]
            area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            candidates.append((area, p1, p2))
    
    candidates.sort(key=lambda x: x[0], reverse=True)
    
    for area, p1, p2 in candidates:
        min_x, max_x = sorted((p1[0], p2[0]))
        min_y, max_y = sorted((p1[1], p2[1]))
        
        mid_x = (min_x + max_x) / 2
        mid_y = (min_y + max_y) / 2
        
        if not is_point_in_polygon(mid_x, mid_y):
            continue
            
        if rect_intersects_edges(min_x, max_x, min_y, max_y):
            continue
            
        return area

with open('day09/input.txt') as f:
    data = f.read().strip()

print("part 1: ", part1(data))
print("part 2: ", part2(data))