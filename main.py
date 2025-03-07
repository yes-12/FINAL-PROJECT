# Example file showing a circle moving on screen
import pygame
import time

# pygame setup
pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
running = True
dt = 0


rect = pygame.Rect(980, 590, 30, 30) 
vel = 5




while running:
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rect.x -= 300 * dt
    if keys[pygame.K_d]:
        rect.x += 300 * dt
    if keys[pygame.K_LEFT]:
        rect.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        rect.x += 300 * dt
    if keys[pygame.K_SPACE]:
        rect.y -= 7
    elif rect.y < 590:
        rect.y += 7
    if rect.x < 0:
        rect.x = 0
    if rect.x > 1250:
        rect.x = 1250
    if rect.y < 0:
        rect.y = 0
    if rect.x < 40:
        if rect.y > 540:
            1==1
    if keys[pygame.K_ESCAPE]:
        print("QUITTING")
        pygame.quit()

    screen.blit(text_surface, (40, 250))
    # or just `render_to` the target surface.
    GAME_FONT.render_to(screen, (40, 350), "Hello World!", (0, 0, 0))

    # flip() the display to put your work on screen
    screen.fill((0, 0, 64))
    gate = pygame.draw.rect(screen, (0,255,0), (0, 540, 40, 80))
    pygame.draw.rect(screen, (64, 64, 64), (0, 620, 1280, 100))
    pygame.draw.circle(screen, (255, 0, 0), rect.center, 15)
    pygame.display.flip()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()