import os
from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)

# Load environment variables from `.env` file if it exists
if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

@app.route('/')
def index():
    # Generar un nuevo número secreto al cargar la página
    session['secret_number'] = random.randint(1, 100)
    session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    # Obtener el número enviado por el usuario
    user_guess = int(request.json['guess'])
    
    # Incrementar el contador de intentos
    session['attempts'] += 1
    
    # Comparar con el número secreto
    secret_number = session.get('secret_number')
    
    if user_guess < secret_number:
        result = "mayor"
    elif user_guess > secret_number:
        result = "menor"
    else:
        result = "correcto"
    
    # Preparar la respuesta
    response = {
        'result': result,
        'attempts': session['attempts']
    }
    
    return jsonify(response)

@app.route('/reset', methods=['POST'])
def reset():
    # Generar un nuevo número secreto
    session['secret_number'] = random.randint(1, 100)
    session['attempts'] = 0
    return jsonify({'message': 'Juego reiniciado'})

if __name__ == '__main__':
    app.run(debug=True)