from flask import Flask, request, jsonify
from game_logic import lanzar_dado

app = Flask(__name__)

@app.route('/lanzar_dado', methods=['POST'])
def lanzar_dado_route():
    data = request.json
    num_caras = data.get('num_caras', 6)
    resultado = lanzar_dado(num_caras)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
