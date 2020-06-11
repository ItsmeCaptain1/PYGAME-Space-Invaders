import pygame
import random
import math

from pygame import mixer


pygame.init()

# create the screen
window_height = 600
window_width = 1000 
screen = pygame.display.set_mode(size=(window_width,window_height))

# Title ans Icon
pygame.display.set_caption("First Game")
icon = pygame.image.load('C:\\Users\\DELL\\Downloads\\ufo.png')
pygame.display.set_icon(icon)

# BackGround Image
BGImg = pygame.image.load("C:\\Users\\DELL\\Downloads\\spaceships-race-outer-space-vector-illustration_107791-2432.jpg")
BGImg = pygame.transform.scale(BGImg,(1000,600))

# Background Sound
mixer.music.load("E:\\space_invaders\\Space-Invaders-Pygame-master\\background.wav")
fire_sound = mixer.Sound("E:\\space_invaders\\fire.wav")
col_sound = mixer.Sound("E:\\space_invaders\\explo.wav")
mixer.music.play(-1)            

# About PLayer
playerImg = pygame.image.load("C:\\Users\\DELL\\Downloads\\jet.png")
playerImg = pygame.transform.scale(playerImg,(50,50))
playerX = 360
playerY = 480
playerX_changer = 0

def player(x,y):
    screen.blit( playerImg, ( x, y ) )

# About Bullet
bulletImg = pygame.image.load("C:\\Users\\DELL\\Downloads\\bullet.png")
bulletImg = pygame.transform.scale(bulletImg,(20,20))
bulletX = playerX
bulletY = playerY
playerAlive = True 
fire = False

def fire_bullet(x,y):
    screen.blit(bulletImg,(x+25-10,y-10))



# About Enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemy = 3
for i in range(number_of_enemy) :
    enemyImg.append(pygame.image.load("C:\\Users\\DELL\\Downloads\\rocksteady.png"))
    enemyImg[i] = pygame.transform.scale(enemyImg[i],(50,50))
    enemyX.append(random.randint(50,900))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(50)

def enemy(x,y,i):
    screen.blit( enemyImg[i], ( x, y ) )
    
# Collision
def isCollision(x1,y1,x2,y2):
    distance = math.sqrt( math.pow( x1-x2 , 2 ) + math.pow( y1-y2 , 2 ) )
    if distance <= 40 :
        return True
    return False 

# score
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf',32)
Xposi_score = 10
Yposi_score = 10

def show_score(x,y) :
    score = score_font.render( "Score : " + str(score_value) , True , (255,255,255) )
    screen.blit(score,(x,y))

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf',48)
Xposi_game_over = 450
Yposi_game_over = 275

def show_game_over(x,y) :
    game_over = game_over_font.render( "Game Over !" , True , (0,255,0) )
    screen.blit(game_over,(x,y))

# Game Loop
running = True

left = True
right = False
while running:
    #pygame.time.delay(5)

    # For backgrond color
    screen.fill((0,0,50))

    # BackGround Image
    screen.blit(BGImg,(0,0))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            
    # if Key is pressed check whether it is left or right 
    keys_press = pygame.key.get_pressed()
    # PLAYER MOVEMENT
    if keys_press[pygame.K_LEFT] and playerX > 50:
        playerX -= 4
    if keys_press[pygame.K_RIGHT] and playerX <= 900 :
        playerX += 4
    
    
    # fire - Bullet is curruntly moving or not
    if fire == False and keys_press[pygame.K_SPACE] :
        fire = True
        fire_sound.play()
        bulletX = playerX
        bulletY = playerY
        
    # BULLET MOVEMENT 
    if fire :
        # if bullet's y position is less then 50 then we disappeare the bullet and fire new bullet
        if bulletY > 50 :
            fire_bullet(bulletX,bulletY)
            bulletY -= 10 
        else : fire = False

    # COLLISION
    for i in range(number_of_enemy) :
        con = isCollision( bulletX , bulletY , enemyX[i] , enemyY[i] )
        if con :
            col_sound.play()
            score_value += 1 
            fire = False
            enemyX[i] = random.randint(50,900)
            enemyY[i] = random.randint(50,150)
            bulletX = playerX
            bulletY = playerY
            

    # ENEMY MOVEMENT
    for i in range(number_of_enemy) :
        if enemyX[i] >= 900 :
            enemyX_change[i] *= (-1)
            enemyY[i] += enemyY_change[i]
        if enemyX[i] <= 50 :
            enemyX_change[i] *= (-1)
            enemyY[i] += enemyY_change[i]
        enemyX[i] += enemyX_change[i]
        if enemyY[i] >= 450 :
            running = False
            show_game_over(Xposi_game_over,Yposi_game_over)
            
        
    for i in range(number_of_enemy) :
        enemy(enemyX[i] , enemyY[i] ,i) 
        
    
       
    player(playerX,playerY)
    show_score(Xposi_score,Yposi_score)
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
