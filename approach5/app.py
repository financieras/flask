# https://gemini.google.com/app/389a17b60450b191?hl=es-ES

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def roll_dice():
    if request.method == 'POST':
        num_faces = int(request.form['num_faces'])
        result = random.randint(1, num_faces)
        return jsonify({'result': result})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)