
import sys
import heapq

def dijkstra(maze, start, goals):
    """
    Perform Dijkstra's algorithm to find the shortest path from start to any of the goals.
    """
    visited = set()
    distances = {start: 0}
    heap = [(0, start)]  # (distance, current)

    while heap:
        current_distance, current = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        x, y = current
        if current in goals:
            path = []
            while current != start:
                for dx, dy, direction in [(0, 1, 'down'), (0, -1, 'up'), (1, 0, 'right'), (-1, 0, 'left')]:
                    new_x, new_y = x - dx, y - dy
                    if (new_x, new_y) in distances and distances[(new_x, new_y)] == distances[current] - 1:
                        path.append(direction)
                        current = (new_x, new_y)
                        break
            path.reverse()
            return path

        # Check possible moves: up, down, left, right
        for dx, dy, _ in [(0, 1, 'down'), (0, -1, 'up'), (1, 0, 'right'), (-1, 0, 'left')]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "1":
                new_pos = (new_x, new_y)
                new_distance = current_distance + 1
                if new_pos not in distances or new_distance < distances[new_pos]:
                    distances[new_pos] = new_distance
                    heapq.heappush(heap, (new_distance, new_pos))

    return None


def read_maze(filename):
    """
    Read the maze from the specified file.
    Returns the maze as a 2D list, robot position, goal positions, and obstacle positions.
    """
    with open(filename) as f:
        maze = []
        initial_pos = None
        goals = []
        obstacles = []
        for line in f:
            content = line.strip()
            if content.startswith("[") and content.endswith("]"):
                # Extract maze dimensions
                dimensions_str = content[1:-1]
                length, width = map(int, dimensions_str.split(","))
                maze = [['0' for _ in range(width)] for _ in range(length)]

            elif content.startswith("(") and content.endswith(")"):
                # Extract robot position
                if initial_pos is None:
                    initial_pos = tuple(map(int, content[1:-1].split(",")))
                    x, y = initial_pos
                    maze[y][x] = "R"  # Mark robot's initial position as "R"
                else:
                    # Extract goal position
                    goals.extend(tuple(map(int, x.strip()[1:-1].split(","))) for x in content.split("|"))
                    for goal in goals:
                        x, y = goal
                        maze[y][x] = "g"  # Mark goal positions as "g"

                    # now read for obstacle positions
                    for next_line in f:
                        next_content = next_line.strip()
                        if "," in next_content:
                            # Strip parentheses before splitting
                            obstacle = tuple(map(int, next_content.strip("()").split(",")))
                            obstacles.append(obstacle)
                            x, y, width, height = obstacle
                            for i in range(y, y + height):
                                for j in range(x, x + width):
                                    maze[i][j] = "1"  # Mark obstacle positions as "1"
                        else:
                            # Stop reading obstacle positions if a new section starts
                            break

        return maze, initial_pos, goals, obstacles


def main():
    if len(sys.argv) != 3:
        print("Usage: python dijkstra_algorithm.py <maze_file> <algorithm_file>")
        sys.exit(1)

    maze_file = sys.argv[1]
    algorithm_file = sys.argv[2]

    maze, initial_pos, goals, _ = read_maze(maze_file)

    print("Maze Representation:")
    for row in maze:
        print(" ".join(cell for cell in row))

    print("\nRobot's Initial Position:", initial_pos)
    print("Goal Positions:")
    for goal in goals:
        print(goal)

    print("\nRunning algorithm...")
    path = dijkstra(maze, initial_pos, goals)

    if path is not None:
        print("\nPath Found:")
        print(" -> ".join(path))
    else:
        print("\nNo path found from robot's initial position to any of the goals.")

    print("\nExecuting algorithm script to display moves...")
    # Execute the algorithm script
    exec(open(algorithm_file).read())


if __name__ == "__main__":
    main()
