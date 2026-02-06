#Welcome to 3D-game!!
#Move around with W A S D
#Look around with left/right arrows
#Press "k" to stop
#Now with textures!

import time
import math
import keyboard
import pygame

rayDis = []
screenW = 1300
screenH = 1000
playerX = 2
playerY = 2
playerHeading = 0
s = 0.05
rayS = 0.01
desiredPlayerY = playerY
desiredPlayerX = playerX
r, g, b = 0, 0, 204
fov = 60
numRays = screenW//10


pygame.init()
screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()


wallTex = [[1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]]


#The map to generate 1 is a wall and 0 is nothing
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#Raycast function

def SendRay(x, y, heading):
    desiredRayX = 0
    desiredRayY = 0
    rayX = x
    rayY = y
    rayHeading = heading
    while True:
        desiredRayX = math.sin(math.radians(rayHeading)) * rayS
        desiredRayY = -math.cos(math.radians(rayHeading)) * rayS

        if map[round(rayY + desiredRayY)][round(rayX)] == 0 and map[round(rayY)][round(rayX + desiredRayX)] == 0:
            rayY += desiredRayY
            rayX += desiredRayX
        else:
            break
    alpha = playerHeading - heading
    if alpha > 180:
        alpha -= 360
    elif alpha <= -180:
        alpha += 360
    if map[round(rayY + desiredRayY)][round(rayX)] == 1:
        wallPer = rayX - math.floor(rayX)
        if -90 < heading <= 90:
            tone = 1
        else:
            tone = 0.5
    elif map[round(rayY)][round(rayX + desiredRayX)] == 1:
        tone = 0.75
        wallPer = rayY - math.floor(rayY)
    rayDis.append([(math.cos(math.radians(alpha)) * (math.sqrt((x - rayX)**2 + (y - rayY)**2))), tone, wallPer])

#Collision detection functions for the player

def CollisionDetX(desX, desY):
    if map[round(playerY)][round(playerX + desX)] == 0:
        return desX
    return 0
    
def CollisionDetY(desX, desY):
    if map[round(playerY + desY)][round(playerX)] == 0:
        return desY
    return 0

#Draws the lines based on player distance

def DrawLine(index, dis):
    if dis[0] != 0:
        size = 1000/dis[0]
    else:
        size = 1000
    texRow = wallTex[int(20 * dis[2])]
    for color_index, color in enumerate(texRow):
        if color == 0:
            r,g,b = 126, 47, 8
        else:
            r,g,b = 145 ,145 ,145
        x = index * 10
        y = screenH / 2 + size / 2 - size / 20 * (color_index + 1)
        pygame.draw.rect(screen, (r * dis[1] ,g * dis[1] ,b * dis[1] ), (x, y, 10, size/20 + 1))


#Main loop, will sleep for 0.05 seconds to reduce lag

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((190, 190, 190))

    #Rotation
    if keyboard.is_pressed("left_arrow"):
        playerHeading -= 3
    if keyboard.is_pressed("right_arrow"):
        playerHeading += 3
    
    if playerHeading > 180:
        playerHeading -= 360
    elif playerHeading <= -180:
        playerHeading += 360

    #Movement
    if keyboard.is_pressed("w"):
        desiredPlayerX = math.sin(math.radians(playerHeading)) * s
        desiredPlayerY = -math.cos(math.radians(playerHeading)) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)
        
    elif keyboard.is_pressed("s"):
        desiredPlayerX = -math.sin(math.radians(playerHeading)) * s
        desiredPlayerY = math.cos(math.radians(playerHeading)) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)
        
    if keyboard.is_pressed("a"):
        desiredPlayerX = -math.cos(math.radians(playerHeading)) * s
        desiredPlayerY = -math.sin(math.radians(playerHeading)) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)
        
    elif keyboard.is_pressed("d"):
        desiredPlayerX = math.cos(math.radians(playerHeading)) * s
        desiredPlayerY = math.sin(math.radians(playerHeading)) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)

    #Stop script

    if keyboard.is_pressed("k"):
        exit()
        break

    rayDis.clear()
    #Send the rays and draw them
    for n in range (numRays):
        rayHeading = playerHeading - (fov / 2) + (n * fov / numRays)
        if rayHeading > 180:
            rayHeading -= 360
        elif rayHeading <= -180:
            rayHeading += 360
        SendRay(playerX, playerY, rayHeading)

    for dis_index, dis in enumerate(rayDis):
        DrawLine(dis_index, dis)
    pygame.display.flip()
    time.sleep(0.02)