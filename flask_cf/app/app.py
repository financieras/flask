from flask import Flask, render_template, request

app = Flask(__name__)

@app.before_request
def before_request_func():
    print('Antes de la petición ...')   # Impresión por la consola del servidor Flask

@app.after_request
def after_request_func(response):
    print("Después de la petición ...")   # Impresión por la consola del servidor Flask
    return response

def index():
    #return "Bienvenidos a Flask"
    print('Estamos realizando  la petición de la ruta raiz ...')   # Impresión por la consola del servidor Flask
    data = {
        'title': 'Index',
        'encabezado': 'Bienvenido'
    }
    return render_template('index.html', data=data)

@app.route('/contacto')
def contacto():
    data = {
        'title': 'Contacto',
        'encabezado': 'Contáctame'
    }
    return render_template('contacto.html', data=data)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'¡Hola, {nombre}!'

@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    return f'La suma de {valor1} y {valor2} es {valor1 + valor2}.'

@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
    return f'Te llamas {nombre} y tienes {edad} años.'

@app.route('/lenguajes')
def lenguajes():
    data={
        'hay_lenguajes': False,
        'lenguajes': ['PHP','Python','Kotlin','Java','C++','JavaScript']
    }
    return render_template('lenguajes.html', data=data)

@app.route('/datos')
def datos():
    print(request.args)   # imprime en la consola del servidor un diccionario inmutable
    lenguaje = request.args.get('valor1')
    año = int(request.args.get('valor2'))
    return f'Continúo aprendiendo {lenguaje} en {año+1} '
    #return 'Estos son los datos'

@app.route('/holaMundo')
def hello_world():
    return '<p>Hello <b>world</b>!</p>'

'''
@app.route('/')
def index():
    return 'Bienvenidos a la página principal'
'''


if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=5000)
