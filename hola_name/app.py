from flask import Flask, request, render_template_string

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def hola_mundo():
    return '<h1>¡¡¡Hola mundo!!!</h1> \
            <p>El formulario está en <a href="/formulario">http://127.0.0.1:5000/formulario</a></p>'

# Ruta para el formulario, acepta métodos GET y POST
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Manejo de la solicitud POST (cuando se envía el formulario)
        nombre = request.form.get('nombre')        
        # Validación: comprobar que el nombre no esté vacío
        if not nombre:
            return 'Por favor, ingresa un nombre válido.', 400  # Retorna un error 400 si el nombre está vacío
        return f'Hola, {nombre}'
    else:
        # Manejo de la solicitud GET (cuando se accede a la página del formulario)
        return '''
            <form method="post">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre">
                <input type="submit" value="Enviar">
            </form>
        '''

# Verifica si este script se está ejecutando directamente
if __name__ == '__main__':
    # Inicia el servidor en modo debug
    app.run(debug=True)

# Instrucciones para lanzar el servidor:
# Lanzar el servidor desde el entorno virtual y desde la carpeta hola_name
# python app.py
# Ir a la página http://127.0.0.1:5000/formulario si se quiere ir directamente al formulario
# La página raiz solo hace un "Hola Mundo"                        