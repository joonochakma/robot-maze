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
