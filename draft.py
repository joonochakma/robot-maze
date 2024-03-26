import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
filename = sys.argv[1]
#method = sys.argv[2]
print (sys.argv[1])

Maze = {}
with open(filename) as f:
    for line in f:
        content = line.strip()
        # print(content)
        content_list = content.split(" ")
        widthOfMaze = content_list[0]
        widthOfMaze1= [int(i) for i in widthOfMaze.split() if i.isdigit()]
        #lengthOfMaze= content_list[1]
        # drivingD = content_list[2]
        # straightD = content_list[3]

    
        # if country_map.get(city1):
        #     city1_list = country_map.get(city1)
        #     city1_list.append((city2, int(drivingD), int(straightD)))
        #     country_map.update({city1:city1_list})
        # else:
        #     country_map.update({city1:[(city2, int(drivingD), int(straightD))]})
            
        # if country_map.get(city2):
        #     city2_list = country_map.get(city2)
        #     city2_list.append((city1, int(drivingD), int(straightD)))
        #     country_map.update({city2:city2_list})
        # else:
        #     country_map.update({city2:[(city1, int(drivingD), int(straightD))]})
            
print(str(widthOfMaze1) + content_list[0])      
# print(country_map)

        

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
 
# widthOfMaze = None
# lengthOfMaze = None
# robot_x = None
# robot_y = None





# # def robotInfo():
# #     with open(filename) as f:
# #         for line in f:
# #             content = line.strip()
# #             if content.startswith("(") and content.endswith(")"):
# #                 coordinates_str = content[1:-1]  # Remove the square brackets
# #                 coordinates = [int(coord) for coord in coordinates_str.split(",")]
# #                 print(coordinates)
# #                 if len(coordinates) == 2:
# #                     robot_x, robot_y = coordinates
# #                     print ("robot y:", robot_y)
# #                     print ("robot x:", robot_x)
# #                     break  # Assuming you want the first pair and exit


# with open(filename) as f:
#     for line in f:
#         content = line.strip()
#         # Assuming the line contains a single pair of coordinates like "[5,11]"
#         if content.startswith("[") and content.endswith("]"):
#             coordinates_str = content[1:-1]  # Remove the square brackets
#             coordinates = [int(coord) for coord in coordinates_str.split(",")]
#             if len(coordinates) == 2:
#                 widthOfMaze, lengthOfMaze = coordinates
#                 break  # Assuming you want the first pair and exit
#             break
#         #it will the robot cords
        
#         elif content.startswith("(") and content.endswith(")"):
#                 print ("passing through")
#                 coordinates_str = content[1:-1]  # Remove the square brackets
#                 coordinates = [int(coord) for coord in coordinates_str.split(",")]
#                 print(coordinates)
#                 if len(coordinates) == 2:
#                     robot_x, robot_y = coordinates
#                     print ("robot y:", robot_y)
#                     print ("robot x:", robot_x)
#                     break  # Assuming you want the first pair and exit

            
# # You can now use widthOfMaze and lengthOfMaze variables
# print("Width of Maze:", widthOfMaze)
# print("Length of Maze:", lengthOfMaze)
# # print ("robot y:", robot_y)
# # print ("robot x:", robot_x)


#Tuesday 26th
# import sys

# filename = sys.argv[1]

# widthOfMaze = None
# lengthOfMaze = None
# robotPosition = None
# goalPositions = []
# obstaclePositions = []

# with open(filename) as f:
#     for line in f:
#         content = line.strip()
#         if content.startswith("[") and content.endswith("]"):
#             # Extract maze dimensions [5,11]
#             dimensions_str = content[1:-1]
#             widthOfMaze, lengthOfMaze = map(int, dimensions_str.split(","))

#         elif content.startswith("(") and content.endswith(")"):
#             # Extract robot position
#             if robotPosition is None:
#                 robotPosition = tuple(map(int, content[1:-1].split(",")))
#             else:
#                 # Extract goal position
#                 goalPositions.extend(tuple(map(int, x.strip()[1:-1].split(","))) for x in content.split("|"))

#                 # After reading a line for goal positions, now read for obstacle positions
#                 for next_line in f:
#                     next_content = next_line.strip()
#                     if "," in next_content:
#                         # Strip parentheses before splitting
#                         obstaclePositions.append(tuple(map(int, next_content.strip("()").split(","))))
#                     else:
#                         # Stop reading obstacle positions if a new section starts
#                         break

# print("Dimensions of the Maze:", widthOfMaze, "x", lengthOfMaze)
# print("Robot's Initial Position:", robotPosition)
# print("Goal Positions:")
# for goal in goalPositions:
#     print(goal)
# print("Obstacle Positions:")
# for obstacle in obstaclePositions:
#     print(obstacle)
