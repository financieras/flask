from flask import Flask, request, jsonify, render_template
from game_logic import HungryMonstersGame

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.json
    height = data.get('height', 18)
    width = data.get('width', 32)
    num_players = data.get('num_players', 3)
    amount_food = data.get('amount_food', 50)
    
    # Crear instancia de HungryMonstersGame
    game = HungryMonstersGame(height, width, num_players, amount_food)
    
    # Inicializar el tablero
    board = game.initialize_board()
    
    return jsonify({'board': board})

if __name__ == '__main__':
    app.run(debug=True)