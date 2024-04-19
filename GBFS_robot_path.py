import sys
import heapq

def heuristic(current, goal):
    """
    Calculate the Manhattan distance heuristic between current position and goal.
    """
    x1, y1 = current
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def solve_path(maze, start, goals):
    """
    Perform Greedy Best-First Search to find a path from start to any of the goals.
    """
    visited = set()
    heap = [(heuristic(start, goals[0]), start, [])]  # (h_cost, current, path)
    visited_count = 0

    while heap:
        _, current, path = heapq.heappop(heap)
        if current in visited:
            continue

        visited.add(current)
        visited_count += 1  # Increment visited count

        x, y = current
        if current in goals:
            print(f"<Node{current}> {visited_count}")
            return path

        # Check possible moves: up, down, left, right
        for dx, dy, direction in [(0, 1, 'down'), (0, -1, 'up'), (1, 0, 'right'), (-1, 0, 'left')]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "1":
                new_pos = (new_x, new_y)
                heapq.heappush(heap, (heuristic(new_pos, goals[0]), new_pos, path + [direction]))

    print("No goal is reachable;", visited_count)
    return None


def main():
    if len(sys.argv) != 2:
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

if __name__ == "__main__":
    main()
