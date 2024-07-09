import cv2 as cv
import numpy as np
from collections import deque
import time

pathFile = open("path.txt", "w+")

flag = False
flag1 = False
flag2 = True
end =[740,300]
path = []

def draw_circle(event,x,y,flags,param):
 
    flag2 = True
    start = (end[0],end[1])
    newPath = []
    if event == cv.EVENT_LBUTTONDOWN:
        
        cv.circle(img,(x,y),1,(0,0,255),-1)
        if not grid[x][y]:
            queue, visited = bfs(start, (x,y) , graph)
            goal = (x,y)
            flag = True
        path_head, path_segment = goal, goal
        if(flag == True):
            while path_segment and path_segment in visited:
                cv.imshow('image',img)
                cv.circle(img,(path_segment[0],path_segment[1]),1,(0,0,255),-1)
                path_segment = visited[path_segment]                
                if path_segment == None:
                    flag1 = True
                    end[0]=x
                    end[1]=y
                    break
                else:
                    newPath.append(path_segment[1])
                    newPath.append(path_segment[0])
            newPath.reverse()
            for i in range(0,len(newPath)-1,1):
                path.append(newPath[i])
                pathFile.write(str(newPath[i])+' ')
    
    if event == cv.EVENT_RBUTTONDOWN:#pathFile.write(str(path_segment[0]) + ' ' + str(path_segment[1]) + ' ')
        pathFile.close()    
            
                
            
        
def Menyat(x,y,flag):
    end = (x,y)
    return True
    
def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return queue, visited

rows = 800
cols = 900

img = np.zeros((rows,cols,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
#12txt
file = open('points2d.txt', 'r')
l = [line.strip() for line in file]
arr = l[0]
array = arr.split() 

x = []
y = []
for i in range(0,len(array),1):
    if i % 2 == 0:
        x.append(float(array[i]))
    elif i % 2 == 1:     
        y.append(float(array[i]))
        file.readline()
#goto(0,0)
#grid?
print(x)
print(y)
cv.circle(img,(int(y[1]+400),int(x[1]+400)),6,(0,0,255),5)
for i in range(0,len(x),1):
    #goto(x[i],y[i])
    if i == len(x)-1:
        break
    cv.line(img,(int(y[i]+400),int(x[i]+400)),(int(y[i+1]+400),int(x[i+1]+400)),(255,0,0),10)
#FIRST ROOM
#cv.line(img,(50,50),(250,50),(255,0,0),23)
#cv.line(img,(250,50),(250,130),(255,0,0),23) 
#cv.line(img,(250,130),(112,130),(255,0,0),23) #справа на лево
#cv.line(img,(172,130),(172,204),(255,0,0),23) # сверхну в низ
#cv.line(img,(172,204),(122,204),(255,0,0),23)# справа в низ
#cv.line(img,(250,130),(250,458),(255,0,0),23) # край сверхну вниз
#cv.line(img,(250,458),(50,458),(255,0,0),23)  #  нижний краф слева на право
#cv.line(img,(50,458),(50,299),(255,0,0),23) # снизу вверх край
#cv.line(img,(50,299),(186,299),(255,0,0),23) # cлева напрвао
#cv.line(img,(186,299),(186,379),(255,0,0),23)  # сверхну вниз
#cv.line(img,(118,299),(118,379),(255,0,0),23) # сверхну вниз
#cv.line(img,(50,299),(50,50),(255,0,0),23)
#cv.line(img,(112,130),(112,140),(255,0,0),23) 
 #cv.circle(img,(int(y[i]+400),int(x[i]+400)),1,(255,0,0),-1)
#Second room
#cv.line(img,(0+350,0+50),(200+350,0+50),(255,0,0),23)
#cv.line(img,(200+350,0+50),(200+350,408+50),(255,0,0),23)
#cv.line(img,(200+350,408+50),(0+350,408+50),(255,0,0),30)
#cv.line(img,(0+350,408+50),(0+350,0+50),(255,0,0),23)
#cv.line(img,(200+350,80+50),(62+350,80+50),(255,0,0),23)
#cv.line(img,(62+350,80+50),(62+350,90+50),(255,0,0),23)
#cv.line(img,(122+350,80+50),(122+350,163+50),(255,0,0),23)
#cv.line(img,(122+350,163+50),(82+350,163+50),(255,0,0),23)
#cv.line(img,(82+350,163+50),(82+350,325+50),(255,0,0),23)
#cv.line(img,(82+350,325+50),(150+350,325+50),(255,0,0),23)
#cv.line(img,(200+350,244+50),(132+350,244+50),(255,0,0),23)

#cv.line(img,(0+650,0+50),(200+650,0+50),(255,0,0),23)
#cv.line(img,(200+650,0+50),(200+650,408+50),(255,0,0),23)
#cv.line(img,(200+650,408+50),(0+650,408+50),(255,0,0),23)
#cv.line(img,(0+650,408+50),(0+650,0+50),(255,0,0),23)
#cv.line(img,(200+650,80+50),(62+650,80+50),(255,0,0),23)
#cv.line(img,(62+650,80+50),(62+650,90+50),(255,0,0),23)
#cv.line(img,(112+650,80+50),(112+650,153+50),(255,0,0),23)
#cv.line(img,(112+650,153+50),(62+650,153+50),(255,0,0),23)
#cv.line(img,(200+650,328+50),(132+650,328+50),(255,0,0),23)
#cv.line(img,(132+650,328+50),(132+650,248+50),(255,0,0),23)
#cv.line(img,(132+650,248+50),(64+650,248+50),(255,0,0),23)
#cv.line(img,(64+650,248+50),(64+650,328+50),(255,0,0),23)

print(img[123][115][0])

grid = [0] * rows
for i in range(rows):
    grid[i] = [0]*cols
    
for i in range(0,len(grid)-1,1):
    for j in range(0,len(grid[i])-1,1):
        if(img[i][j][0] == 255):
            grid[i][j] = 1
            
print(grid[123][115])
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

start = (end[0],end[1])
goal = start
queue = deque([start])
visited = {start: None}


while True:

    cv.imshow('image',img)




    if cv.waitKey(20)& 0xFF == 27:
        break
cv.destroyAllWindows()

    
