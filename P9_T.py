import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

invisible_man = pygame.Rect(10,10,100,100)

change = 10
#for quiz
    screen.fill((255,255,255))
    
    # Condition when i reaches 20 or greater, pause a second and close the screen
    
    pygame.draw.rect(screen, (0,0,0), invisible_man)        
    
    # change the x,y coordinates
    
    pygame.display.update()
    pygame.time.delay(100)