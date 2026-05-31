import pygame

from aircraft import Aircraft
from physics import integrate
from constants import *

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

aircraft = Aircraft()

running = True

while running:

    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    integrate(aircraft, dt)

    screen.fill((30, 30, 40))

    pygame.draw.line(
        screen,
        (0, 255, 0),
        (0, GROUND_Y),
        (WIDTH, GROUND_Y),
        3
    )

    x = int(aircraft.pos[0])
    y = int(aircraft.pos[1])

    pygame.draw.polygon(
        screen,
        (255, 255, 255),
        [
            (x + 20, y),
            (x - 20, y - 10),
            (x - 20, y + 10)
        ]
    )

    pygame.display.flip()

pygame.quit()