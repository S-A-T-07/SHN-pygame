import pygame

# Main Game function
def MainGameFunction():

    #? pygame setup
    pygame.init()

    #? Varible
    size    = (1280, 720)
    BGCOLOR = (255, 255, 255)
    
    #? Character 
    #* sprite 
    character = pygame.image.load('assets/zombieGreen.png')

    #* sprite position
    x = 50
    y = 50

    #* sprite size
    width = 40
    height = 60

    #* sprite velocity
    vel = 10
    
    # Config 
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Zombie Zone")

    clock = pygame.time.Clock()

    # Main game Loop
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

        screen.blit(character, (x, y, width, height))
        
        pygame.display.update()

        screen.fill(BGCOLOR)

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()