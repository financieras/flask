document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('diceForm');
    const resultDiv = document.getElementById('result');
    const facesResultSpan = document.getElementById('facesResult');
    const diceResultSpan = document.getElementById('diceResult');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        
        try {
            const response = await fetch('/', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();

            // Actualizar el resultado en la página
            facesResultSpan.textContent = data.faces;
            diceResultSpan.textContent = data.result;
            resultDiv.classList.remove('hidden');

            // Animación simple del dado
            diceResultSpan.classList.add('dice-roll');
            setTimeout(() => {
                diceResultSpan.classList.remove('dice-roll');
            }, 500);

        } catch (error) {
            console.error('Error:', error);
            alert('Hubo un error al lanzar el dado. Por favor, intenta de nuevo.');
        }
    });
});