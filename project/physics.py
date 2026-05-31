import numpy as np
from constants import *

def compute_forces(aircraft):
    speed = np.linalg.norm(aircraft.vel)

    thrust = np.array([PLANE_THRUST, 0])

    drag = np.array([
        -DRAG_COEFF * speed * aircraft.vel[0],
        -DRAG_COEFF * speed * aircraft.vel[1]
    ])

    weight = np.array([0, PLANE_MASS * GRAVITATIONAL_ACCELERATION])

    lift = np.array([
        0,
        -LIFT_COEFF * speed**2
    ])

    return {
        "thrust": thrust,
        "drag": drag,
        "lift": lift,
        "weight": weight
    }

def integrate(aircraft, dt):
    forces = compute_forces(aircraft)

    total_force = (
        forces["thrust"]
        + forces["drag"]
        + forces["lift"]
        + forces["weight"]
    )

    aircraft.acc = total_force / PLANE_MASS
    aircraft.vel += aircraft.acc * dt
    aircraft.pos + aircraft.vel * dt;

    if aircraft.pos[1] > GROUND_Y:
        aircraft.pos[1] = GROUND_Y
        if aircraft.vel[1] > 0:
            aircraft.vel[1] = 0

    return forces