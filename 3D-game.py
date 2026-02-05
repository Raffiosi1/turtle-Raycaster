#Welcome to 3D-game!!
#Move around with W A S D
#Press "k" to stop

import time
import turtle
import math
import keyboard

rayDis = []
screenW = 1300
screenH = 1000
playerX = 2
playerY = 2
playerHeading = 0
s = 0.1
rayS = 0.01
desiredPlayerY = playerY
desiredPlayerX = playerX
r, g, b = 0, 0, 0.8
fov = 60
numRays = screenW//10

turtle.clear()
turtle.setup(width=screenW, height=screenH)
turtle.color(r, g, b)
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(1)
turtle.tracer(0)
turtle.penup()

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

#Function to help draw map

def Square():
    turtle.penup()
    turtle.goto(turtle.xcor() + 25, turtle.ycor() + 25)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.begin_fill()
    for n in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

#Raycast function

def SendRay(x, y, heading):
    desiredRayX = 0
    desiredRayY = 0
    rayX = x
    rayY = y
    rayHeading = heading
    while True:
        if 0 < rayHeading <= 90:
            desiredRayY = -math.sin(math.radians(90 - abs(rayHeading))) * rayS
            desiredRayX = math.cos(math.radians(90 - abs(rayHeading))) * rayS
        elif 90 < rayHeading <= 180:
            desiredRayY = math.cos(math.radians(180 - abs(rayHeading))) * rayS
            desiredRayX = math.sin(math.radians(180 - abs(rayHeading))) * rayS
        elif -180 < rayHeading <= -90:
            desiredRayY = math.cos(math.radians(180 - abs(rayHeading))) * rayS
            desiredRayX = -math.sin(math.radians(180 - abs(rayHeading))) * rayS
        elif -90 < rayHeading <= 0:
            desiredRayY = -math.sin(math.radians(90 - abs(rayHeading))) * rayS
            desiredRayX = -math.cos(math.radians(90 - abs(rayHeading))) * rayS
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
        if -90 < heading <= 90:
            tone = 1
        else:
            tone = 0.5
    elif map[round(rayY)][round(rayX + desiredRayX)] == 1:
        tone = 0.75
    rayDis.append([(math.cos(math.radians(alpha)) * (math.sqrt((x - rayX)**2 + (y - rayY)**2))), tone])

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
    turtle.color(r * dis[1], g * dis[1], b * dis[1])
    turtle.penup()
    turtle.setheading(90)
    turtle.goto((index * 2 - screenW//10)*5 + 5, -size/2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()


#Main loop, will sleep for 0.05 seconds to reduce lag

while True:
    turtle.clear()
    turtle.color(r, g, b)

    #Rotation
    if keyboard.is_pressed("a"):
        playerHeading -= 5
    if keyboard.is_pressed("d"):
        playerHeading += 5
    
    if playerHeading > 180:
        playerHeading -= 360
    elif playerHeading <= -180:
        playerHeading += 360

    #Movement
    if keyboard.is_pressed("w"):
        if 0 < playerHeading <= 90:
            desiredPlayerY = -math.sin(math.radians(90 - abs(playerHeading))) * s
            desiredPlayerX = math.cos(math.radians(90 - abs(playerHeading))) * s
        elif 90 < playerHeading <= 180:
            desiredPlayerY = math.cos(math.radians(180 - abs(playerHeading))) * s
            desiredPlayerX = math.sin(math.radians(180 - abs(playerHeading))) * s
        elif -180 < playerHeading <= -90:
            desiredPlayerY = math.cos(math.radians(180 - abs(playerHeading))) * s
            desiredPlayerX = -math.sin(math.radians(180 - abs(playerHeading))) * s
        elif -90 < playerHeading <= 0:
            desiredPlayerY = -math.sin(math.radians(90 - abs(playerHeading))) * s
            desiredPlayerX = -math.cos(math.radians(90 - abs(playerHeading))) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)
    elif keyboard.is_pressed("s"):
        if 0 < playerHeading <= 90:
            desiredPlayerY = math.sin(math.radians(90 - abs(playerHeading))) * s
            desiredPlayerX = -math.cos(math.radians(90 - abs(playerHeading))) * s
        elif 90 < playerHeading <= 180:
            desiredPlayerY = -math.cos(math.radians(180 - abs(playerHeading))) * s
            desiredPlayerX = -math.sin(math.radians(180 - abs(playerHeading))) * s
        elif -180 < playerHeading <= -90:
            desiredPlayerY = -math.cos(math.radians(180 - abs(playerHeading))) * s
            desiredPlayerX = math.sin(math.radians(180 - abs(playerHeading))) * s
        elif -90 < playerHeading <= 0:
            desiredPlayerY = math.sin(math.radians(90 - abs(playerHeading))) * s
            desiredPlayerX = math.cos(math.radians(90 - abs(playerHeading))) * s
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
    turtle.update()
    time.sleep(0.05)