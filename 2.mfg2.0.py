import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
 
pygame.display.set_caption("First Game")

x = 50
y = 450
width = 50
height = 50
vel = 25
screenwidth = 500
isJump = False
jumpCount = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x <= screenwidth - width - vel:
        x += vel

    if keys[pygame.K_UP] and y >= vel:
        y -= vel

    if keys[pygame.K_DOWN] and  y <= screenwidth - height - vel:
        y += vel

    if keys[pygame.K_SPACE] :
            if jumpCount > 0 :
                y = y - (jumpCount)**2
                jumpCount = jumpCount - 1

            else :  
                if y <= screenwidth - height - vel :
                    y = y + (jumpCount)**2
                    jumpCount = jumpCount - 1
                else :
                    break



    win.fill(0)
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()

pygame.quit()