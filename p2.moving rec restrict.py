import pygame
pygame.init()

screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Walking Rectangle")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run :
    pygame.time.delay(100)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - vel >= 0 :
        x = x - vel
    if keys[pygame.K_RIGHT] and x <= screen_width - width - vel  :
        x = x + vel
    if keys[pygame.K_UP] and y - vel >= 0 :
        y = y - vel
    if keys[pygame.K_DOWN] and y <= screen_height - height - vel  :
        y = y + vel
    
    win.fill(0)
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()

pygame.quit()
