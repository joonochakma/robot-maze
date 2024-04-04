import sys

filename = sys.argv[1]

widthOfMaze = None
lengthOfMaze = None
robotPosition = None
goalPositions = []
obstaclePositions = []
maze = None

with open(filename) as f:
    for line in f:
        content = line.strip()
        if content.startswith("[") and content.endswith("]"):
            # Extract maze dimensions 
            dimensions_str = content[1:-1]
            lengthOfMaze, widthOfMaze = map(int, dimensions_str.split(","))
            # "_" is a throwaway variable
            maze = [['0' for _ in range(widthOfMaze)] for _ in range(lengthOfMaze)]

        elif content.startswith("(") and content.endswith(")"):
            # Extract robot position
            if robotPosition is None:
                robotPosition = tuple(map(int, content[1:-1].split(",")))
                x, y = robotPosition
                maze[y][x] = "R"  # Mark robot's initial position as "R"
            else:
                # Extract goal position
                goalPositions.extend(tuple(map(int, x.strip()[1:-1].split(","))) for x in content.split("|"))
                for goal in goalPositions:
                    x, y = goal
                    maze[y][x] = "g"  # Mark goal positions as "g"

                # After reading a line for goal positions, now read for obstacle positions
                for next_line in f:
                    next_content = next_line.strip()
                    if "," in next_content:
                        # Strip parentheses before splitting
                        obstacle = tuple(map(int, next_content.strip("()").split(",")))
                        obstaclePositions.append(obstacle)
                        x, y, width, height = obstacle
                        for i in range(y, y + height):
                            for j in range(x, x + width):
                                if 0 <= i < lengthOfMaze and 0 <= j < widthOfMaze:
                                    maze[i][j] = "1"  # Mark obstacle positions as "1"
                    else:
                        # Stop reading obstacle positions if a new section starts
                        break

print("Dimensions of the Maze:", lengthOfMaze, "x", widthOfMaze)
print("Robot's Initial Position:", robotPosition)
print("Goal Positions:")
for goal in goalPositions:
    print(goal)
print("Obstacle Positions:")
for obstacle in obstaclePositions:
    print(obstacle)

print("Maze Representation:")
for row in maze:
    print(row)
