# Example file shoscreeng a basic pygame "game loop"
import pygame


def MainGameFunction():

    # pygame setup
    pygame.init()

    # Varible
    size    = (1280, 720)
    BGCOLOR = (255, 255, 255)
    
    x = 50
    y = 50
    width = 50
    height = 50
    vel = 5
    
    
    # walkRight = [pygame.image.load('assets/zombieGreen.png')]
    # walkLeft = [pygame.image.load('assets/zombieGreen.png')]
    
    left = False
    right = False
    walkCount = 0
    
    # # Config 
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Zombie Zone")

    clock = pygame.time.Clock()


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

        if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel



        pygame.draw.rect(screen, (255,0,0), (x, y, width, height))  #This takes: screendow/surface, color, rect 
        pygame.display.update()

        screen.fill(BGCOLOR)

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    
    pygame.quit()