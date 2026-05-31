import numpy as np
from constants import GROUND_Y

class Aircraft:
    def __init__(self):
        self.pos = np.array([100.0, GROUND_Y])
        self.vel = np.array([0.0, 0.0])
        self.acc = np.array([0.0, 0.0])