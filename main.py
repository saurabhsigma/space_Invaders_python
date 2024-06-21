# importing all the required libraries 

import math
import random
import pygame
# Classes for loading Sound objects and managing playback are included in the mixer library.
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,500))

# background
background = pygame.image.load('background.png')

# Set the background color to black
background_color = (0, 0, 0)

# sound 
mixer.music.load("background.mp3")
mixer.music.play(-1)

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.jpeg")
pygame.display.set_icon(icon)

# player - look and position
playerImg = pygame.image.load("player.jpeg")
playerX = 370
playerY = 380
playerX_change = 0

# enemy - look and position
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies  = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.jpeg'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)


# bullet
# ready - you cant see the bullet on the screen
#  fire - the bullet is currently moving

bulletImg = pygame.image.load('bullet.jpeg')
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# score 
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over 
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# game loop 
running = True
while running:
    # RGB = red, green ,blue
    screen.fill((0,0,0))
    # background image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # if a keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.sound('laser.wav')
                    bulletSound.play()
                    # get the current x cordinate of the spaceship 
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
        
        for i in range(num_of_enemies):
            # Game Over 
            if enemyY[i] > 340:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                    game_over_text()
                    break
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 380
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
            enemy(enemyX[i], enemyY[i], i)
        # Bullet Movement
        if bulletY <= 0:
            bulletY = 380
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

        
        


print("just a checker that everything runs fine...")
