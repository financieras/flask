# https://www.perplexity.ai/search/como-funcionan-las-peticiones-DNraKD1HQuOrHpnWNimhyA

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])    # Definimos una ruta '/' que maneja tanto peticiones GET como POST
def roll_dice():
    if request.method == 'POST':            # Para POST, procesamos la tirada del dado.
        # Obtener el número de caras del dado del formulario
        faces = request.form.get('faces', type=int, default=6)  # Obtenemos el número de caras del dado del formulario. 6 por defecto.
        
        # Validar que el número de caras sea al menos 2
        if faces < 2:
            faces = 2
        
        # Generar un número aleatorio
        result = random.randint(1, faces)
        
        # Devolver como JSON el resultado y el número de caras.
        return jsonify({'result': result, 'faces': faces})
    
    # Si es una petición GET, renderizar la plantilla
    return render_template('index.html')    # Para GET, simplemente renderizamos la plantilla 'index.html'.

if __name__ == '__main__':
    app.run(debug=True)


# La respuesta JSON permite una fácil integración con JavaScript en el frontend para actualizar la interfaz de usuario dinámicamente.