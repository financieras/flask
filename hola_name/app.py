from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '<h1>¡¡¡Hola mundo!!!</h1> \
            <p>El formulario está en <a href="/formulario">http://127.0.0.1:5000/formulario</a></p>'

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Manejo de la solicitud POST
        nombre = request.form.get('nombre')
        return f'Hola, {nombre}'
    else:
        # Manejo de la solicitud GET
        return '''
            <form method="post">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre">
                <input type="submit" value="Enviar">
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)

# Lanzar el servidor desde el entorno virtual y desde la carpeta hola_name
# Ir a la página http://127.0.0.1:5000/formulario y no a la página raiz