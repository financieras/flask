# https://claude.ai/chat/7c06804a-a01b-46b1-bbde-06d003095cc3

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        faces = int(request.form.get('faces', 6))
        result = random.randint(1, faces)
        return jsonify({'result': result})
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
