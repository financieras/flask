# https://chatgpt.com/c/66fe4720-e67c-800f-9b1f-58dd2212b1e4

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll', methods=['POST'])
def roll_dice():
    data = request.get_json()
    sides = data.get('sides', 6)  # Obtiene el número de caras, por defecto 6
    result = random.randint(1, sides)  # Genera el número aleatorio
    return jsonify({'result': result})  # Devuelve el resultado en formato JSON

if __name__ == '__main__':
    app.run(debug=True)
