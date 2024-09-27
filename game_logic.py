import random

class Juego:
    def __init__(self, num_caras=6):
        self.num_caras = num_caras

    def hacer_tirada(self):
        return random.randint(1, self.num_caras)

