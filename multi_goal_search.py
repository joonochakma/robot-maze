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

    while goals:
        current_goal = goals[0]
        path = solve_path(maze, initial_pos, [current_goal])

        if path is not None:
            print( "['" + "' , '".join(path) + "']")
            print("\n")
            # Update robot's position to the goal position
            initial_pos = current_goal
            # Remove the goal from the list of goals
            goals.remove(current_goal)
        else:
            print("\nNo path found from robot's current position to the current goal.")

    print("\nNo more goals to reach.")
    # Execute the algorithm script
    exec(open(algorithm_file).read())





    path = solve_path(maze, initial_pos, goals)

        
    

    

if __name__ == "__main__":
    main()
