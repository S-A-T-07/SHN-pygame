import pygame

# Main Game function
def MainGameFunction():

    #? pygame setup
    pygame.init()

    #? Varible
    size    = (1080, 720)
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
    vel = 5
    
    # Config 
    screen = pygame.display.set_mode( size )
    pygame.display.set_caption( "Zombie Zone" )

    clock = pygame.time.Clock()

    # Main game Loop
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

        if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
            x -= vel

        if keys[pygame.K_RIGHT] and x < 1000 - vel - width:  # Making sure the top right corner of our character is less than the screen width - its width 
            x += vel

        if keys[pygame.K_UP] and y > vel:  # Same principles apply for the y coordinate
            y -= vel

        if keys[pygame.K_DOWN] and y < 700 - height - vel:
            y += vel

        screen.blit(character, (x, y, width, height))
        
        pygame.display.update()

        screen.fill(BGCOLOR)

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()