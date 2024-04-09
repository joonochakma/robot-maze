import sys
from collections import deque

def bfs(maze, start, goals):
    """
    Perform Breadth-First Search to find a path from start to any of the goals.
    """
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        if current in visited:
            continue

        visited.add(current)

        x, y = current
        if current in goals:
            return path

        # Check possible moves: up, down, left, right
        for dx, dy, direction in [(0, 1, 'down'), (0, -1, 'up'), (1, 0, 'right'), (-1, 0, 'left')]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "1":
                queue.append(((new_x, new_y), path + [direction]))

    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python bfs_algorithm.py <maze_file>")
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

    path = bfs(maze, robot_pos, goal_positions)

    if path is not None:
        print("\nPath Found:")
        print(" -> ".join(path))
    else:
        print("\nNo path found from robot's initial position to any of the goals.")


if __name__ == "__main__":
    main()