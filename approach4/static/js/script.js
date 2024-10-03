document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('diceForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const sides = document.getElementById('sides').value;

        try {
            const response = await fetch('/roll', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ sides: parseInt(sides, 10) })
            });

            const data = await response.json();
            resultDiv.innerHTML = `<h2>Resultado: ${data.result}</h2>`;
        } catch (error) {
            resultDiv.innerHTML = `<h2>Error al lanzar el dado</h2>`;
        }
    });
});
