from flask import Flask, request, jsonify, render_template
from game_logic import Juego    # importamos la clase Juego, de ella usaremos el método hacer_tirada

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lanzar_dado', methods=['POST'])
def lanzar_dado_route():
    data = request.json
    num_caras = data.get('num_caras', 6)
    
    # Crear instancia de Juego
    mi_juego = Juego(num_caras)    # instanciamos mi_juego
    
    # Usar el método de la clase
    resultado = mi_juego.hacer_tirada() # invocamos el método hacer_tirada de la clase Juego  
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
