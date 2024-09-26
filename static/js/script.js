document.addEventListener('DOMContentLoaded', () => {
    const numCarasInput = document.getElementById('numCaras');
    const jugarBtn = document.getElementById('jugarBtn');
    const resultadoP = document.getElementById('resultado');

    jugarBtn.addEventListener('click', () => {
        const numCaras = parseInt(numCarasInput.value);
        
        fetch('/lanzar_dado', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ num_caras: numCaras }),
        })
        .then(response => response.json())
        .then(data => {
            resultadoP.textContent = `Resultado: ${data.resultado}`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultadoP.textContent = 'Ocurrió un error al lanzar el dado.';
        });
    });
});
