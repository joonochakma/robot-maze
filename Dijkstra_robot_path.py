# import sys
# from heapq import heappop, heappush

# def dijkstra(maze, start, goals):
#     """
#     Perform Dijkstra's algorithm to find the shortest path from start to any of the goals.
#     """
#     def neighbors(x, y):
#         """
#         Get valid neighbors of a cell (x, y).
#         """
#         for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             new_x, new_y = x + dx, y + dy
#             if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "1":
#                 yield new_x, new_y

#     visited = set()
#     queue = [(0, start, [])]  # Priority queue with (cost, position, path)
#     visited_count = 0

#     while queue:
#         cost, current, path = heappop(queue)
#         if current in visited:
#             continue

#         visited.add(current)
#         visited_count += 1

#         x, y = current
#         if current in goals:
#             print("Total Visited Nodes:", visited_count)
#             return path

#         for neighbor_x, neighbor_y in neighbors(x, y):
#             new_cost = cost + 1  # Uniform cost for all moves
#             heappush(queue, (new_cost, (neighbor_x, neighbor_y), path + [(neighbor_x, neighbor_y)]))

#     print("Total Visited Nodes:", visited_count)
#     return None

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: python dijkstra_algorithm.py <maze_file>")
#         sys.exit(1)

#     maze_file = sys.argv[1]
#     with open(maze_file) as f:
#         maze = [list(line.strip()) for line in f]

#     robot_pos = None
#     goal_positions = []
#     for y in range(len(maze)):
#         for x in range(len(maze[y])):
#             if maze[y][x] == "R":
#                 robot_pos = (x, y)
#             elif maze[y][x] == "g":
#                 goal_positions.append((x, y))

#     path = dijkstra(maze, robot_pos, goal_positions)

#     if path is not None:
#         print("\nPath Found:")
#         print(" -> ".join(str(pos) for pos in path))
#     else:
#         print("\nNo path found from robot's initial position to any of the goals.")

# if __name__ == "__main__":
#     main()




import sys
from heapq import heappop, heappush

def dijkstra(maze, start, goals):
    """
    Perform Dijkstra's algorithm to find the shortest path from start to any of the goals.
    """
    def neighbors(x, y):
        """
        Get valid neighbors of a cell (x, y).
        """
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "1":
                yield new_x, new_y

    visited = set()
    queue = [(0, start, [])]  # Priority queue with (cost, position, path)
    visited_count = 0

    while queue:
        cost, current, path = heappop(queue)
        if current in visited:
            continue

        visited.add(current)
        visited_count += 1

        x, y = current
        if current in goals:
            print("Total Visited Nodes:", visited_count)
            return path

        for neighbor_x, neighbor_y in neighbors(x, y):
            new_cost = cost + 1  # Uniform cost for all moves
            heappush(queue, (new_cost, (neighbor_x, neighbor_y), path + [(neighbor_x, neighbor_y)]))

    print("Total Visited Nodes:", visited_count)
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python dijkstra_algorithm.py <maze_file>")
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

    path = dijkstra(maze, robot_pos, goal_positions)

    if path is not None:
        print("\nPath Found:")
        print(" -> ".join(str(pos) for pos in path))
    else:
        print("\nNo path found from robot's initial position to any of the goals.")

if __name__ == "__main__":
    main()
