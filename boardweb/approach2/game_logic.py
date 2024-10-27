import random
from enum import Enum
from typing import List, Tuple, Dict, Optional
from abc import ABC, abstractmethod

class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

class Strategy(ABC):
    """Clase abstracta base para las estrategias de movimiento"""
    @abstractmethod
    def get_next_move(self, game: 'HungryMonstersGame', player_pos: Tuple[int, int]) -> Optional[Direction]:
        """
        Determina el siguiente movimiento según la estrategia.
        
        Args:
            game: Instancia del juego actual
            player_pos: Posición actual del jugador como tupla (y, x)
            
        Returns:
            Direction opcional. None si no hay movimiento posible
        """
        pass

class RandomStrategy(Strategy):
    """Estrategia de movimiento aleatorio"""
    def get_next_move(self, game: 'HungryMonstersGame', player_pos: Tuple[int, int]) -> Optional[Direction]:
        valid_moves = []
        for direction in Direction:
            new_pos = (
                player_pos[0] + direction.value[0],
                player_pos[1] + direction.value[1]
            )
            if game.is_valid_move(new_pos):
                valid_moves.append(direction)
        
        return random.choice(valid_moves) if valid_moves else None

class NearestFoodStrategy(Strategy):
    """Estrategia de buscar la comida cercana de mayor valor"""
    def get_next_move(self, game: 'HungryMonstersGame', player_pos: Tuple[int, int]) -> Optional[Direction]:
        best_direction = None
        max_food_value = -1

        # Revisar todas las direcciones posibles
        for direction in Direction:
            new_pos = (
                player_pos[0] + direction.value[0],
                player_pos[1] + direction.value[1]
            )
            
            if game.is_valid_move(new_pos):
                cell_value = game.get_food_value(new_pos)
                if cell_value > max_food_value:
                    max_food_value = cell_value
                    best_direction = direction

        # Si no se encontró comida, usar movimiento aleatorio
        if best_direction is None:
            random_strategy = RandomStrategy()
            return random_strategy.get_next_move(game, player_pos)
            
        return best_direction


class HungryMonstersGame:
    def __init__(self, height: int, width: int, num_players: int, amount_food: int):
        self.height = height
        self.width = width
        self.num_players = num_players
        self.amount_food = amount_food
        self.board = None
        self.scores = {chr(65 + i): 0 for i in range(num_players)}  # A:0, B:0, C:0, ...
        self.player_positions = {}  # Almacena la posición de cada jugador
        self.current_player_index = 0
        self.strategies = {
            'random': RandomStrategy(),
            'nearest_food': NearestFoodStrategy()
        }

    def initialize_board(self) -> List[List[str]]:
        # Crear un tablero vacío
        self.board = [['·' for _ in range(self.width)] for _ in range(self.height)]

        # Colocar jugadores
        players = [chr(65 + i) for i in range(self.num_players)]
        for player in players:
            self._place_player(player)

        # Colocar comida
        num_food_cells = max(1, int((self.height * self.width - self.num_players) * self.amount_food / 100))
        self._place_food(num_food_cells)

        return self.board

    def _place_player(self, player: str) -> None:
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == '·':
                self.board[y][x] = player
                self.player_positions[player] = (y, x)
                break
    
    def _place_food(self, num_food_cells: int) -> None:
        empty_cells = [(y, x) for y in range(self.height) 
                      for x in range(self.width) if self.board[y][x] == '·']
        for _ in range(min(num_food_cells, len(empty_cells))):
            y, x = empty_cells.pop(random.randint(0, len(empty_cells) - 1))
            self.board[y][x] = str(random.randint(1, 9))

    def is_valid_move(self, pos: Tuple[int, int]) -> bool:
        """Verifica si una posición es válida para moverse"""
        y, x = pos
        # Verificar límites del tablero
        if not (0 <= y < self.height and 0 <= x < self.width):
            return False
        # Verificar que la celda esté vacía o contenga comida
        return self.board[y][x] == '·' or self.board[y][x].isdigit()

    def get_food_value(self, pos: Tuple[int, int]) -> int:
        """Obtiene el valor de la comida en una posición"""
        y, x = pos
        if 0 <= y < self.height and 0 <= x < self.width and self.board[y][x].isdigit():
            return int(self.board[y][x])
        return -1

    def get_current_player(self) -> str:
        """Obtiene el jugador actual"""
        return chr(65 + self.current_player_index)

    def move_player(self, strategy_name: str) -> Dict:
        """Mueve al jugador actual según la estrategia especificada"""
        player = self.get_current_player()
        current_pos = self.player_positions[player]
        
        # Obtener la estrategia
        strategy = self.strategies.get(strategy_name, self.strategies['random'])
        
        # Obtener la dirección del movimiento
        direction = strategy.get_next_move(self, current_pos)
        
        if direction:
            new_y = current_pos[0] + direction.value[0]
            new_x = current_pos[1] + direction.value[1]
            
            # Si hay comida, actualizar puntuación
            if self.board[new_y][new_x].isdigit():
                self.scores[player] += int(self.board[new_y][new_x])
            
            # Actualizar el tablero
            self.board[current_pos[0]][current_pos[1]] = '·'
            self.board[new_y][new_x] = player
            self.player_positions[player] = (new_y, new_x)
        
        # Actualizar el turno
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        
        # Verificar si el juego ha terminado
        game_over = all(not cell.isdigit() for row in self.board for cell in row)
        
        return {
            'board': self.board,
            'scores': self.scores,
            'current_player': self.get_current_player(),
            'game_over': game_over,
            'winner': self._get_winner() if game_over else None
        }

    def _get_winner(self) -> str:
        """Determina el ganador del juego"""
        max_score = max(self.scores.values())
        winners = [player for player, score in self.scores.items() if score == max_score]
        return winners[0] if len(winners) == 1 else "Empate entre " + ", ".join(winners)

    def get_game_state(self) -> Dict:
        """Obtiene el estado actual del juego"""
        return {
            'board': self.board,
            'scores': self.scores,
            'current_player': self.get_current_player(),
            'game_over': all(not cell.isdigit() for row in self.board for cell in row)
        }