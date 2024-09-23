from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, Mundo!'

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    datos = {
        'mensaje': 'Estos son algunos datos de ejemplo',
        'números': [1, 2, 3, 4, 5]
    }
    return jsonify(datos)

@app.route('/api/enviar', methods=['POST'])
def recibir_datos():
    datos_recibidos = request.json
    print(f"Datos recibidos: {datos_recibidos}")
    return jsonify({'mensaje': 'Datos recibidos correctamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)