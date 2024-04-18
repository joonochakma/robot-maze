from collections import deque

def solve_path(maze, start, goals):
    """
    Perform Beam Search to find a path from start to any of the goals.
    """
    visited = set()
    queue = deque([(start, [])])
    visited_count = 0

    while queue:
        current, path = queue.popleft()
        if current in visited:
            continue

        visited.add(current)
        visited_count += 1

        x, y = current
        if current in goals:
            print("Total Visited Nodes:", visited_count)
            return path

        # Check possible moves: up, down, left, right
        for dx, dy, direction in [(0, 1, 'down'), (0, -1, 'up'), (1, 0, 'right'), (-1, 0, 'left')]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "1":
                queue.append(((new_x, new_y), path + [direction]))
    
    print("Total Visited Nodes:", visited_count)
    return None
