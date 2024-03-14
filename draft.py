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

        
