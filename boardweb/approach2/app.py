from flask import Flask, request, jsonify, render_template, session
from game_logic import HungryMonstersGame
import uuid

app = Flask(__name__)
app.secret_key = 'hungry_monsters_secret_key'  # Necesario para manejar sesiones

# Diccionario para almacenar las instancias del juego
games = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    try:
        data = request.json
        height = data.get('height', 18)
        width = data.get('width', 32)
        num_players = data.get('num_players', 3)
        amount_food = data.get('amount_food', 50)
        
        # Validar datos de entrada
        if not (5 <= height <= 27 and 6 <= width <= 48 and 
                2 <= num_players <= 26 and 0 <= amount_food <= 100):
            return jsonify({'error': 'Valores de entrada inválidos'}), 400
        
        # Crear nueva instancia del juego
        game = HungryMonstersGame(height, width, num_players, amount_food)
        
        # Generar ID único para el juego
        game_id = str(uuid.uuid4())
        games[game_id] = game
        
        # Inicializar el tablero
        board = game.initialize_board()
        
        # Guardar ID del juego en la sesión
        session['game_id'] = game_id
        
        return jsonify({
            'game_id': game_id,
            'board': board,
            'scores': game.scores,
            'current_player': game.get_current_player(),
            'game_over': False
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/make_move', methods=['POST'])
def make_move():
    try:
        game_id = session.get('game_id')
        if not game_id or game_id not in games:
            return jsonify({'error': 'No hay juego activo'}), 400
        
        data = request.json
        strategy = data.get('strategy', 'random')  # Por defecto usa estrategia random
        
        game = games[game_id]
        if strategy not in game.strategies:
            return jsonify({'error': 'Estrategia no válida'}), 400
        
        # Realizar movimiento
        game_state = game.move_player(strategy)
        
        # Si el juego terminó, limpiamos la sesión
        if game_state['game_over']:
            del games[game_id]
            session.pop('game_id', None)
        
        return jsonify(game_state)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/game_state', methods=['GET'])
def get_game_state():
    try:
        game_id = session.get('game_id')
        if not game_id or game_id not in games:
            return jsonify({'error': 'No hay juego activo'}), 400
        
        game = games[game_id]
        return jsonify(game.get_game_state())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)