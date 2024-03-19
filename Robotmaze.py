import sys

filename = sys.argv[1]

widthOfMaze = None
lengthOfMaze = None
robotPosition = None
goalPositions = []
obstaclePositions = []

with open(filename) as f:
    for line in f:
        content = line.strip()
        if content.startswith("[") and content.endswith("]"):
            # Extract maze dimensions [5,11]
            dimensions_str = content[1:-1]
            widthOfMaze, lengthOfMaze = map(int, dimensions_str.split(","))

        elif content.startswith("(") and content.endswith(")"):
            # Extract robot position
            if robotPosition is None:
                robotPosition = tuple(map(int, content[1:-1].split(",")))
            else:
                # Extract goal position
                goalPositions.extend(tuple(map(int, x.strip()[1:-1].split(","))) for x in content.split("|"))

                # After reading a line for goal positions, now read for obstacle positions
                for next_line in f:
                    next_content = next_line.strip()
                    if "," in next_content:
                        # Strip parentheses before splitting
                        obstaclePositions.append(tuple(map(int, next_content.strip("()").split(","))))
                    else:
                        # Stop reading obstacle positions if a new section starts
                        break

print("Dimensions of the Maze:", widthOfMaze, "x", lengthOfMaze)
print("Robot's Initial Position:", robotPosition)
print("Goal Positions:")
for goal in goalPositions:
    print(goal)
print("Obstacle Positions:")
for obstacle in obstaclePositions:
    print(obstacle)
