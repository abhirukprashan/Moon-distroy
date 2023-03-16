import pygame
import math
import random

pygame.init()

#creating screen
screen = pygame.display.set_mode((400, 600))

#background
background = pygame.image.load('background.jpg')

#Title and icon
pygame.display.set_caption("Moon distory")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player
player_image = pygame.image.load('space.png')
player_image = pygame.transform.scale(player_image, (80, 80))
playerX = 170
playerY = 510
player_changer = 0

#enermy
Enermy_image =[]
enermyX = []
enermyY = []
enermyX_changer = []
enermyY_changer = []
num_of_enemies = random.randint(6,15)



for i in range(num_of_enemies):
    Enermy_image.append(pygame.image.load('monster.png'))    
    enermyX.append(random.randint(0, 335))
    enermyY.append(random.randint(50, 150))
    enermyX_changer.append(0.8)
    enermyY_changer.append(40)

#bullet
bullet_image = pygame.image.load('bullet.png')
bullet_image = pygame.transform.scale(bullet_image, (32, 32))
bulletX = 0
bulletY = 480
bulletX_changer = 0
bulletY_changer = 2
bullet_state = "ready"


#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 42)

textX = 100
textY = 20

#gameover text

over_font = pygame.font.Font('freesansbold.ttf', 62)


def show_score(x, y):
    score = font.render("MOONS: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (70, 300))
def player(x, y):
    screen.blit(player_image, (x, y))

def enermy(x, y, i):
    screen.blit(Enermy_image[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 13, y + 10))

def iscollision(enermyX, enermyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enermyX- bulletX,2))+ (math.pow(enermyY-bulletY,2)))
    if distance < 30:
        return True
    else:
        return False

    
 

#gameloop
running = True

while running:
    screen.fill((255, 0, 0))
    #backgorund
    screen.blit(background, (0, 0))
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    #movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_changer = -3
            if event.key == pygame.K_d:
                player_changer = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_changer = 0


    #player
    playerX += player_changer
    if playerX <=0:
        playerX = 0
    elif playerX >=336:
        playerX = 336



    #enermy
    for i in range(num_of_enemies):


        #gameOver
        if enermyY[i] > 480:
            for j in range(num_of_enemies):
                enermyY[j] = 2000
            game_over_text()
            break

        #enermy movement
        enermyX[i] += enermyX_changer[i]
        if enermyX[i] <=0:
            enermyX_changer[i] = 0.3
            enermyY[i] += enermyY_changer[i]
        elif enermyX[i] >= 339:
            enermyX_changer[i] = -0.3
            enermyY[i] += enermyY_changer[i]

        #collision
        collision = iscollision(enermyX[i],enermyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1 
            enermyX[i] = random.randint(0, 335)
            enermyY[i] = random.randint(50, 150)

        enermy(enermyX[i], enermyY[i], i)

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_changer

    

    
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
