# https://groq.com

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Configuración inicial
num_caras = 6

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global num_caras
        num_caras = int(request.form['num_caras'])
        resultado = random.randint(1, num_caras)
        return jsonify({'resultado': resultado})
    return render_template('index.html', num_caras=num_caras)

if __name__ == '__main__':
    app.run(debug=True)