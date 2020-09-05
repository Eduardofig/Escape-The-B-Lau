import pygame
pygame.init()

#Variables:
x = 500
y = 500
width = 69
height = 60
vel = 15
keys = pygame.key.get_pressed()
scr_width = 1920
scr_height = 1080
is_jump = False
run = True
Jump_Count = 10
Walk_Left = [pygame.image.load('William_left1.png'),pygame.image.load('William_left2.png'),pygame.image.load('William_left3.png'),pygame.image.load('William_left4.png')]
Walk_Right = [pygame.image.load('William_right1.png'),pygame.image.load('William_right2.png'),pygame.image.load('William_right3.png'),pygame.image.load('William_right4.png')]
bg = pygame.image.load('bg.jpg')
character = pygame.image.load('William_char.png')
left = False
right = False

#Drawing
def redraw_game_window ():
    global WalkCount
    win.blit(bg, (0, 0),)
    if WalkCount + 1 >= 12:
        WalkCount = 0
    if left:
        win.blit(Walk_Left[WalkCount//3], (x, y))
        WalkCount += 1
    elif right:
        win.blit(Walk_Right[WalkCount//3], (x, y))
        WalkCount += 1
    else:
        win.blit(character, (x, y))
    pygame.display.update()

#Window setting:
win = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Escape the Bilau')

while run:

    pygame.time.delay(10) #Framerate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

#Movement:
    if keys[pygame.K_DOWN] and y < scr_width - (width + vel):
        y += vel
        #down = True
        #up = False

    if keys[pygame.K_UP] and y > vel:
        y -= vel
        #up = True
        #down = False

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < scr_width - (width + vel):
        x += vel
        right = True
        left = False
    else :
        right = False
        left = False
        WalkCount = 0

#Jumping :
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            WalkCount = 0
    else:
        if Jump_Count >= -10:
            neg = 1
            if Jump_Count <0:
                neg = -1
            y -= (Jump_Count ** 2) * neg * 0.9
            Jump_Count -= 1
        else:
            is_jump = False
            Jump_Count = 10

    redraw_game_window()