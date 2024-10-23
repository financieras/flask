from flask import Flask, request, render_template, flash
from typing import Union, List
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'clave-secreta-app-educativa'  # Necesario para flash messages

def validar_numero(valor: str) -> Union[float, None]:
    """
    Valida y convierte un string a número float.
    
    Args:
        valor (str): String a convertir
        
    Returns:
        float: Número convertido o None si no es válido
    """
    try:
        if valor.strip():  # Verificar que no esté vacío
            return float(valor)
        return None
    except ValueError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Maneja la ruta principal de la aplicación.
    GET: Muestra el formulario
    POST: Procesa la suma de números
    """
    result = None
    
    if request.method == 'POST':
        try:
            # Obtener valores del formulario
            valores: List[str] = request.form.getlist('valor')
            
            # Validar y convertir números
            numeros = [num for valor in valores if (num := validar_numero(valor)) is not None]
            
            # Verificar que hay números para sumar
            if not numeros:
                flash('Error: Por favor, introduce al menos un número válido', 'error')
            else:
                result = sum(numeros)
                flash(f'¡Operación exitosa! Se sumaron {len(numeros)} números', 'success')
                logger.info(f'Suma realizada: {numeros} = {result}')
                
        except Exception as e:
            flash(f'Error inesperado: {str(e)}', 'error')
            logger.error(f'Error en el procesamiento: {str(e)}')
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)