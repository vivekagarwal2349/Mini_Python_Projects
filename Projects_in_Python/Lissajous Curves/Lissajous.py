import pygame 
import math
pygame.init()


pts = []
screen = pygame.display.set_mode((800,800))
grid_width = 80
w, h = pygame.display.get_surface().get_size()
cols = int(w/grid_width)
rows = int(h/grid_width)

clock = pygame.time.Clock()

def display_grid() :
    for i in range(cols) :
        pygame.draw.line(screen, (255,255,255), (i*grid_width+grid_width, 0), (i*grid_width+grid_width, h))
    for i in range(rows) :
        pygame.draw.line(screen, (255,255,255), (0, i*grid_width+grid_width), (w, i*grid_width+grid_width))


def circles (angle) :
    lines_1 = []
    lines_2 = []
    for i in range(1,cols) :
        cx = i*grid_width + (grid_width/2)
        cy = grid_width/2
        radius = grid_width/2-5
        pygame.draw.circle(screen, (255,255,255), (cx,cy), radius, width =1)
        x = radius*math.cos(math.radians(angle*i))
        y = radius*math.sin(math.radians(angle*i))
        pygame.draw.circle(screen, (255,255,255), (cx+x, cy+y), 5)
        pygame.draw.line(screen, (150,150,150), (cx+x, cy+y), (cx+x, h))
        a = 1
        b = 0
        c = int(-(cx+x))
        lines_1.append([a,b,c])
    
    for i in range(1,rows) :
        cy = i*grid_width + (grid_width/2)
        cx = grid_width/2
        radius = grid_width/2-5
        pygame.draw.circle(screen, (255,255,255), (cx,cy), radius, width =1)
        x = radius*math.cos(math.radians(angle*i))
        y = radius*math.sin(math.radians(angle*i))
        pygame.draw.circle(screen, (255,255,255), (cx+x, cy+y), 5)
        pygame.draw.line(screen, (150,150,150), (cx+x, cy+y), (w, cy+y))
        a = 0
        b = 1
        c = int(-(cy+y))
        lines_2.append([a,b,c])

    # print("------------lines 1--------------------------")
    # print(lines_1)
    # print("------------lines 2--------------------------")
    # print(lines_2)
    for i in range(len(lines_1)) :
        a_1 = lines_1[i][0]
        b_1 = lines_1[i][1]
        c_1 = lines_1[i][2]
        for j in range(len(lines_2)) :
            a_2 = lines_2[j][0]
            b_2 = lines_2[j][1]
            c_2 = lines_2[j][2]
            x = int((b_1*c_2 - c_1*b_2)/(a_1*b_2-a_2*b_1))
            y = int((c_1*a_2 - c_2*a_1)/(a_1*b_2-a_2*b_1))
            pts.append([x,y])

    for point in pts :
        pygame.draw.circle(screen, (255,255,255), (point[0],point[1]), 1)
    # print("-----------------Points-------------------------")
    # print(pts)

running = True
angle = 0
while running :

    screen.fill((0,0,0))
    #display_grid()
    circles(angle)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running  = False
    angle+=0.5
    if angle > 370 :
        angle = 0
        pts = []
    #clock.tick(100)
    pygame.display.update()

