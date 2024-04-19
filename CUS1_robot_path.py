import sys

def solve_path(maze, start, goals):
    """
    Perform Iterative Deepening Depth-First Search to find a path from start to any of the goals.
    """
    def dfs(node, path, depth, visited_count, current_coords):
        x, y = node
        if node in visited or depth < 0:
            return None

        visited.add(node)
        visited_count += 1  # Increment the visited count

        if node in goals:
            current_coords = node  # Update current_coords to the coordinates of the goal reached
            print(f"<Node{current_coords}> {visited_count}")  # Print the current node and visited count
            return path

        for dx, dy, direction in [(0, 1, 'down'), (0, -1, 'up'), (1, 0, 'right'), (-1, 0, 'left')]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "1":
                result = dfs((new_x, new_y), path + [direction], depth - 1, visited_count, current_coords)
                if result is not None:
                    return result

        return None

    max_depth = 0
    while True:
        visited = set()
        result = dfs(start, [], max_depth, 0, start)  # Start the count from 0 and pass start coordinates
        if result is not None:
            
            return result
        max_depth += 1
       
    print("none2")
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

    path = solve_path(maze, robot_pos, goal_positions)

    if path is not None:
        print("\nPath Found:")
        print(" -> ".join(path))
    else:
        print("\nNo path found from robot's initial position to any of the goals.")
