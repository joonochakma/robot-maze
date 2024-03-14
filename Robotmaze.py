import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
filename = sys.argv[1]

widthOfMaze = None
lengthOfMaze = None

with open(filename) as f:
    for line in f:
        content = line.strip()
        # Assuming the line contains a single pair of coordinates like "[5,11]"
        if content.startswith("[") and content.endswith("]"):
            coordinates_str = content[1:-1]  # Remove the square brackets
            coordinates = [int(coord) for coord in coordinates_str.split(",")]
            if len(coordinates) == 2:
                widthOfMaze, lengthOfMaze = coordinates
                break  # Assuming you want the first pair and exit
        
# You can now use widthOfMaze and lengthOfMaze variables
print("Width of Maze:", widthOfMaze)
print("Length of Maze:", lengthOfMaze)
