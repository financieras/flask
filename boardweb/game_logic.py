import random

class HungryMonstersGame:
    def __init__(self, height, width, num_players, amount_food):
        self.height = height
        self.width = width
        self.num_players = num_players
        self.amount_food = amount_food
        self.board = None

    def initialize_board(self):
        # Crear un tablero vacío
        self.board = [['·' for _ in range(self.width)] for _ in range(self.height)]

        # Colocar jugadores
        players = [chr(65 + i) for i in range(self.num_players)]  # A, B, C, ...
        for player in players:
            self._place_player(player)

        # Colocar comida
        num_food_cells = max(1, int((self.height * self.width - self.num_players) * self.amount_food / 100))
        self._place_food(num_food_cells)

        return self.board

    def _place_player(self, player):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == '·':
                self.board[y][x] = player
                break
    
    def _place_food(self, num_food_cells):
        empty_cells = [(x, y) for y in range(self.height) for x in range(self.width) if self.board[y][x] == '·']
        for _ in range(min(num_food_cells, len(empty_cells))):
            x, y = empty_cells.pop(random.randint(0, len(empty_cells) - 1))
            self.board[y][x] = str(random.randint(1, 9))


    # Aquí añadiremos más métodos para la lógica del juego, como mover jugadores, comer comida, etc.