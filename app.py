from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        try:
            # Obtenemos todos los valores como una lista
            valores = request.form.getlist('valor')
            
            # Convertimos los valores a float
            numeros = [float(valor) for valor in valores if valor]
            
            # Realizamos la suma
            result = sum(numeros)
            
            # Si no hay números, lanzamos una excepción
            if not numeros:
                raise ValueError("No se proporcionaron números válidos")
                
        except ValueError as e:
            result = f"Error: {str(e)}"
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)