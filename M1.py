import pygame
'''
class Dino:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_hurdle(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, self.rect)
'''
pygame.init()
screen = pygame.display.set_mode((1200, 400))
'''
dino = pygame.image.load("sprites/trex1.png")

dino_rect = Dino(100, 250, 64, 64)
'''
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ''' 
    dino_rect.paste_image(dino)
    '''
    pygame.display.update()
    pygame.time.delay(1)
