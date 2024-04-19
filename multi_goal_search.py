import sys
import importlib.util

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
                    goals.append(initial_pos)  # Add initial position to the list of goals
                else:
                    # Extract goal position
                    goals.extend(tuple(map(int, x.strip()[1:-1].split(","))) for x in content.split("|"))
                    for goal in goals:
                        x, y = goal
                        maze[y][x] = "G"  # Mark goal positions as "G"

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



def calculate_distance(point1, point2):
    """
    Calculate the Manhattan distance between two points.
    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def nearest_neighbor_tsp(graph, start_node):
    """
    Using the Nearest Neighbor method.
    """
    # Initialize a list to store the path
    path = []

    # Create a set to keep track of visited nodes
    visited = set()

    # Start from the specified start node
    current_node = start_node
    path.append(current_node)
    visited.add(current_node)

    # Repeat until all nodes are visited
    while len(visited) < len(graph):
        # Find the nearest unvisited neighbor
        nearest_neighbor = min((neighbor for neighbor in graph if neighbor not in visited),
                               key=lambda neighbor: graph[current_node][neighbor])
        # Move to the nearest neighbor
        current_node = nearest_neighbor
        path.append(current_node)
        visited.add(current_node)

    # Complete the cycle by returning to the start node
    path.append(start_node)

    return path

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
        
    maze_file = sys.argv[1]
    algorithm_name = sys.argv[2]

    # Dynamically import solve_path function from the provided algorithm file
    algorithm_file = algorithm_name + "_robot_path.py"
    spec = importlib.util.spec_from_file_location("solve_path_module", algorithm_file)
    solve_path_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solve_path_module)
    
    if not hasattr(solve_path_module, "solve_path"):
        print(f"Error: 'solve_path' function not found in {algorithm_file}")
        sys.exit(1)
        
    solve_path = solve_path_module.solve_path

    maze, initial_pos, goals, _ = read_maze(maze_file)
    print('.' + "\\" + sys.argv[1] + ' ' + sys.argv[2])

    print("Maze Representation:")
    for row in maze:
        print(" ".join(cell for cell in row))
    print("\n")

    # Create a distance matrix representing the distances between goals
    graph = {}
    for i, goal1 in enumerate(goals):
        graph[i] = {}
        for j, goal2 in enumerate(goals):
            if i != j:
                distance = calculate_distance(goal1, goal2)
                graph[i][j] = distance

    # Find the nearest neighbor path starting from the robot's initial position
    start_node = goals.index(initial_pos)
    nearest_neighbor_path_indices = nearest_neighbor_tsp(graph, start_node)

    # Start from the robot's initial position
    current_pos = initial_pos

    for node_index in nearest_neighbor_path_indices:
        goal = goals[node_index]
        # Find the path from the current position to the current goal
        path = solve_path(maze, current_pos, [goal])
        if path is not None:
            
            print( "['" + "' , '".join(path) + "']")
            
            # Update the current position to the current goal
            current_pos = goal
        else:
            print("\nNo path found from robot's current position to the current goal.")

    print("\nNo more goals to reach.")
    # Execute the algorithm script
    exec(open(algorithm_file).read())


if __name__ == "__main__":
    main()



#  if path is not None:
#             # Convert the path coordinates into directions
#             directions = convert_to_directions(path)
#             # Print the path taken
#             print("Path taken:")
#             print( "['" + "' , '".join(path) + "']")
#             print("\n")
#             # Update robot's position to the goal position