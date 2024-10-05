document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('diceForm');
    const resultDiv = document.getElementById('result');
    const diceResult = document.getElementById('diceResult');

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
            
            diceResult.textContent = `El dado cayó en: ${data.result}`;
            resultDiv.classList.remove('hidden');
        } catch (error) {
            console.error('Error:', error);
            diceResult.textContent = 'Hubo un error al lanzar el dado. Por favor, intenta de nuevo.';
            resultDiv.classList.remove('hidden');
        }
    });
});