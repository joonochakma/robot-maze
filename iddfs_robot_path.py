import sys

def solve_path(maze, start, goals):
    """
    Perform Iterative Deepening Depth-First Search to find a path from start to any of the goals.
    """
    def dfs(node, path, depth):
        x, y = node
        if node in visited or depth < 0:
            return None

        visited.add(node)

        if node in goals:
            return path

        for dx, dy, direction in [(0, 1, 'down'), (0, -1, 'up'), (1, 0, 'right'), (-1, 0, 'left')]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "1":
                result = dfs((new_x, new_y), path + [direction], depth - 1)
                if result is not None:
                    return result

        return None

    max_depth = 0
    while True:
        visited = set()
        result = dfs(start, [], max_depth)
        if result is not None:
            print("Total Visited Nodes:", len(set(result)))
            return result
        max_depth += 1

    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python IDDFS_robot_path.py <maze_file>")
        sys.exit(1)

    maze_file = sys.argv[1]

    with open(maze_file) as f:
        maze = [list(line.strip()) for line in f]

    robot_pos = None
    goal_positions = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "R":
                robot_pos = (x, y)
            elif maze[y][x] == "g":
                goal_positions.append((x, y))

    path = iddfs(maze, robot_pos, goal_positions)

    if path is not None:
        print("\nPath Found:")
        print(" -> ".join(path))
    else:
        print("\nNo path found from robot's initial position to any of the goals.")
