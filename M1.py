import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 400))

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.update()
    pygame.time.delay(1)
