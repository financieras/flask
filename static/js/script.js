// Espera a que todo el contenido del DOM esté completamente cargado antes de ejecutar el script
document.addEventListener('DOMContentLoaded', () => {
    // Obtiene el campo de entrada para el número de caras del dado
    const numCarasInput = document.getElementById('numCaras');
    
    // Obtiene el botón "Jugar"
    const jugarBtn = document.getElementById('jugarBtn');
    
    // Obtiene el párrafo donde se mostrará el resultado
    const resultadoP = document.getElementById('resultado');

    // Agrega un evento 'click' al botón "Jugar"
    jugarBtn.addEventListener('click', () => {
        // Convierte el valor del campo de entrada a un número entero
        const numCaras = parseInt(numCarasInput.value);
        
        // Realiza una solicitud POST al servidor Flask en la ruta '/lanzar_dado'
        fetch('/lanzar_dado', {
            method: 'POST', // Especifica que la solicitud es de tipo POST
            headers: {
                'Content-Type': 'application/json', // Indica que el cuerpo de la solicitud es en formato JSON
            },
            // Envía el número de caras como un objeto JSON en el cuerpo de la solicitud
            body: JSON.stringify({ num_caras: numCaras }),
        })
        // Maneja la respuesta del servidor
        .then(response => {
            // Verifica si la respuesta fue exitosa
            if (!response.ok) {
                throw new Error('Red no válida');
            }
            return response.json(); // Convierte la respuesta a formato JSON
        })
        .then(data => {
            // Muestra el resultado del lanzamiento en el párrafo correspondiente
            resultadoP.textContent = `Resultado: ${data.resultado}`;
        })
        .catch(error => {
            // Maneja errores de red o de respuesta
            console.error('Error:', error);
            resultadoP.textContent = 'Ocurrió un error al lanzar el dado.'; // Muestra un mensaje de error al usuario
        });
    });
});
