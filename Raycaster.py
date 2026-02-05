#Welcome to Raycaster!!
#Move around with arrow keys, up and down to move, left and right to rotate
#Press "k" to stop

from time import *
from turtle import *
from math import *
import keyboard

global playerX
global playerY
global playerHeading
global s
global rayS
global screenW
global screenH
global desiredPlayerX
global desiredPlayerY
global map
global rayDis

rayDis = []
screenW = 1300
screenH = 1000
playerX = 2
playerY = 2
playerHeading = 0
s = 0.001
rayS = 0.001
desiredPlayerY = playerY
desiredPlayerX = playerX

clear()
setup(width=screenW, height=screenH)
speed(0)
hideturtle()
pensize(1)
tracer(0)
penup()

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
    penup()
    goto(xcor() + 25, ycor() + 25)
    setheading(-90)
    pendown()
    begin_fill()
    for n in range(4):
        forward(50)
        right(90)
    end_fill()
    penup()

#Raycast function

def SendRay(x, y, heading):
    desiredRayX = 0
    desiredRayY = 0
    rayX = x
    rayY = y
    rayHeading = heading
    while True:
        if 0 < rayHeading <= 90:
            desiredRayY = -degrees(sin(radians(90 - abs(rayHeading)))) * rayS
            desiredRayX = degrees(cos(radians(90 - abs(rayHeading)))) * rayS
        elif 90 < rayHeading <= 180:
            desiredRayY = degrees(cos(radians(180 - abs(rayHeading)))) * rayS
            desiredRayX = degrees(sin(radians(180 - abs(rayHeading)))) * rayS
        elif -180 < rayHeading <= -90:
            desiredRayY = degrees(cos(radians(180 - abs(rayHeading)))) * rayS
            desiredRayX = -degrees(sin(radians(180 - abs(rayHeading)))) * rayS
        elif -90 < rayHeading <= 0:
            desiredRayY = -degrees(sin(radians(90 - abs(rayHeading)))) * rayS
            desiredRayX = -degrees(cos(radians(90 - abs(rayHeading)))) * rayS
        if map[round(rayY + desiredRayY)][round(rayX)] == 0 and map[round(rayY)][round(rayX + desiredRayX)] == 0:
            rayY += desiredRayY
            rayX += desiredRayX
        else:
            break
    penup()
    color("blue")
    goto(x * 50, -y * 50)
    pendown()
    goto(rayX * 50, -rayY * 50)
    penup()
    color("black")
    rayDis.append(sqrt((rayX - x)**2 + (rayY - y)**2))

#Collision detection functions for the player

def CollisionDetX(desX, desY):
    if map[round(playerY)][round(playerX + desX)] == 0:
        return desX
    return 0
    
def CollisionDetY(desX, desY):
    if map[round(playerY + desY)][round(playerX)] == 0:
        return desY
    return 0

#Main loop, will sleep for 0.05 seconds to reduce lag

while True:
    clear()

    #Rotation
    if keyboard.is_pressed("left arrow"):
        playerHeading -= 10
    if keyboard.is_pressed("right arrow"):
        playerHeading += 10
    
    if playerHeading > 180:
        playerHeading -= 360
    elif playerHeading <= -180:
        playerHeading += 360

    #Movement
    if keyboard.is_pressed("up arrow"):
        if 0 < playerHeading <= 90:
            desiredPlayerY = -degrees(sin(radians(90 - abs(playerHeading)))) * s
            desiredPlayerX = degrees(cos(radians(90 - abs(playerHeading)))) * s
        elif 90 < playerHeading <= 180:
            desiredPlayerY = degrees(cos(radians(180 - abs(playerHeading)))) * s
            desiredPlayerX = degrees(sin(radians(180 - abs(playerHeading)))) * s
        elif -180 < playerHeading <= -90:
            desiredPlayerY = degrees(cos(radians(180 - abs(playerHeading)))) * s
            desiredPlayerX = -degrees(sin(radians(180 - abs(playerHeading)))) * s
        elif -90 < playerHeading <= 0:
            desiredPlayerY = -degrees(sin(radians(90 - abs(playerHeading)))) * s
            desiredPlayerX = -degrees(cos(radians(90 - abs(playerHeading)))) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)
    elif keyboard.is_pressed("down arrow"):
        if 0 < playerHeading <= 90:
            desiredPlayerY = degrees(sin(radians(90 - abs(playerHeading)))) * s
            desiredPlayerX = -degrees(cos(radians(90 - abs(playerHeading)))) * s
        elif 90 < playerHeading <= 180:
            desiredPlayerY = -degrees(cos(radians(180 - abs(playerHeading)))) * s
            desiredPlayerX = -degrees(sin(radians(180 - abs(playerHeading)))) * s
        elif -180 < playerHeading <= -90:
            desiredPlayerY = -degrees(cos(radians(180 - abs(playerHeading)))) * s
            desiredPlayerX = degrees(sin(radians(180 - abs(playerHeading)))) * s
        elif -90 < playerHeading <= 0:
            desiredPlayerY = degrees(sin(radians(90 - abs(playerHeading)))) * s
            desiredPlayerX = degrees(cos(radians(90 - abs(playerHeading)))) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)

    #Stop script

    if keyboard.is_pressed("k"):
        exit()
        break

    #Draw player
    penup()
    goto(playerX * 50, -playerY * 50)
    pensize(5)
    dot()
    pensize(1)
    #Draw map
    for row_index, row in enumerate(map):
        for num_index, num in enumerate(row):
            goto(num_index * 50, -row_index * 50)
            if num == 1:
                Square()

    rayDis.clear()
    #Send the rays and draw them
    for n in range (-screenW // 20, screenW // 20 + 1):
        rayHeading = n + playerHeading
        if rayHeading > 180:
            rayHeading -= 360
        elif rayHeading <= -180:
            rayHeading += 360
        SendRay(playerX, playerY, rayHeading)
    update()
    sleep(0.05)