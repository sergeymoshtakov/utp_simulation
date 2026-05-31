import numpy as np

class Aircraft:
    def __init__(self):
        self.pos = np.array([100.0, 500.0])
        self.vel = np.array([0.0, 0.0])
        self.acc = np.array([0.0, 0.0])