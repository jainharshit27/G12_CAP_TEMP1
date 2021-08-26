import pygame

class Dino:
    def __init__(self, x, y, h, w):
        # Create a rectangle under this method
    
    def draw_hurdle(self, surface):
        # Draw the rectangle under this method
    
    def paste_image(self, image):
        # Paste the image of rectangle under this method
        
# Add Cactus class for creating and drawing a rectangle and pasting an image over it

pygame.init()
screen = pygame.display.set_mode((1200, 400))

dino = pygame.image.load("sprites/trex1.png")
# load images for cactus and ground also

dino_rect = Dino(100, 250, 64, 64)
# create cactus rectangle object using class
# Create Rectangle for ground

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    dino_rect.paste_image(dino)
    # Paste Cactus image using object and class
    # Paste the image of ground
    
    pygame.display.update()
    pygame.time.delay(1)
