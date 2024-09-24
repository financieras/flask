from flask import Flask, request, jsonify
#from main import Juego

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, Mundo!'

@app.route('/api/algoritmos', methods=['GET'])
def enviar_algoritmos():
    datos = {
        'algorithm': ['random', 'close_target','paht_finder']
    }
    return jsonify(datos)

'''
@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    # recoger los datos iniciales que vienen del JavaScript
    mijuego = Juego(NUM_PLAYERS, AMOUNT_FOOD)
    result = mijuego.datos_iniciales(height=18, width=32, num_players=2, amount_food=7)    
    return result
'''

@app.route('/api/enviar', methods=['POST'])
def recibir_datos():
    datos_recibidos = request.json
    print(f"Datos recibidos: {datos_recibidos}")
    return jsonify({'mensaje': 'Datos recibidos correctamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)