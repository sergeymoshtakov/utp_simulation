import pygame
import numpy as np
from aircraft import Aircraft
from physics import integrate
from constants import *

pygame.init()

pygame.display.set_caption("2D Aircraft Physics Simulation")

font = pygame.font.SysFont(None, 28)

WIDTH = 1200
HEIGHT = 700

SCREEN_GROUND_Y = GROUND_OFFSET_Y

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

aircraft = Aircraft()

running = True

while running:

    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    forces = integrate(aircraft, dt)

    screen.fill((30, 30, 40))

    pygame.draw.line(
        screen,
        (0, 255, 0),
        (0, SCREEN_GROUND_Y),
        (WIDTH, SCREEN_GROUND_Y),
        3
    )

    x = int(aircraft.pos[0] * SCALE)
    y = int((aircraft.pos[1] - GROUND_Y) * SCALE + GROUND_OFFSET_Y)

    pygame.draw.polygon(
        screen,
        (255, 255, 255),
        [
            (x + 20, y),
            (x - 20, y - 10),
            (x - 20, y + 10)
        ]
    )

    # print forces

    speed = np.linalg.norm(aircraft.vel)
    lift_force = abs(forces["lift"][1])
    weight_force = abs(forces["weight"][1])
    drag_force = np.linalg.norm(forces["drag"])
    thrust_force = np.linalg.norm(forces["thrust"])
    altitude = GROUND_Y - aircraft.pos[1]

    lines = [
        f"Speed: {speed:.1f} m/s",
        f"Altitude: {altitude:.1f} m",
        f"Thrust: {thrust_force:.0f} N",
        f"Drag: {drag_force:.0f} N",
        f"Lift: {lift_force:.0f} N",
        f"Weight: {weight_force:.0f} N",
    ]
    
    for i, line in enumerate(lines):

        text = font.render(line, True, (255,255,255))

        screen.blit(
            text,
            (20, 20 + i * 30)
        )

    pygame.display.flip()

pygame.quit()