import heapq
import math
import argparse

def parseopt():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--maze', type=argparse.FileType('r'), help='maze file')
    parser.add_argument('-p', '--path', type=str, help='path output file')
    parser.add_argument('-n', '--nodes', type=str, help='nodes output file')
    args = parser.parse_args()
    return args

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(' '.join(str(cell) for cell in line) + '\n')
            
def h1(node, goal):
    return 0

def h2(node, goal):
    return abs(goal[0] - node[0]) + abs(goal[1] - node[1])

def h3(node, goal):
    return math.sqrt((goal[0] - node[0]) ** 2 + (goal[1] - node[1]) ** 2)
    
def paint(first, second, symbol):
    for i,j in second:
        first[i][j] = symbol

def a_star_algorithm(maze, start, goal):
    prio_que = []
    heapq.heappush(prio_que, (h1(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    closed_set = set()
    nodes1 = []

    nodes = [row[:] for row in maze]
    path = [row[:] for row in maze]
    #see until it breaks
    while prio_que:
        current_f, current_g, current_pos = heapq.heappop(prio_que)
        nodes1.append(current_pos)
        
        if current_pos == goal:
            path1 = [current_pos]
            while current_pos in came_from:
                current_pos = came_from[current_pos]
                path1.append(current_pos)
            path1.reverse()
            paint(path, path1, 2)
            paint(nodes, nodes1, 3)
            nodes.insert(0, [2,0,8,0,6,0,4,6])
            path.insert(0, [2,0,8,0,6,0,4,6])
            return path, nodes

        closed_set.add(current_pos)
        
        # see see all possible option
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current_pos[0] + dx, current_pos[1] + dy)

            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 0 and neighbor not in closed_set:
                temp_g_score = current_g + 1

                if temp_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current_pos
                    g_score[neighbor] = temp_g_score
                    f_score = temp_g_score + h1(neighbor, goal)
                    heapq.heappush(prio_que, (f_score, temp_g_score, neighbor))

    
    paint(nodes, nodes1, 3)   
    nodes.insert(0, [2,0,8,0,6,0,4,6])
    return [], nodes

maze = [
    [0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0]
]
args = parseopt()

if args.maze:
    dimensions = next(args.maze).strip().split()
    width, height = int(dimensions[0]), int(dimensions[1])
    
    maze = [list(map(int, line.strip().split())) for line in args.maze]
    
    start = (0, 0)
    goal = (height-1, width-1)

    start = (0, 0)
    goal = (goal[0], goal[1])
    path, nodes = a_star_algorithm(maze, start, goal)
    if args.path:
        save_to_file(args.path, path)
    if args.nodes:
        save_to_file(args.nodes, nodes)
    print(path)
    print(nodes)
    
else:
    path, nodes = a_star_algorithm(maze, (0, 0), (4, 4))
    if args.path:
        save_to_file(args.path, path)
    if args.nodes:
        save_to_file(args.nodes, nodes)

    print(path)
    print(nodes)
