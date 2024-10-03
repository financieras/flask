document.addEventListener('DOMContentLoaded', () => {
    const guessInput = document.getElementById('guessInput');
    const guessButton = document.getElementById('guessButton');
    const message = document.getElementById('message');
    const attempts = document.getElementById('attempts');
    const resetButton = document.getElementById('resetButton');

    let gameOver = false;

    guessButton.addEventListener('click', makeGuess);
    resetButton.addEventListener('click', resetGame);

    function makeGuess() {
        if (gameOver) return;

        const guess = parseInt(guessInput.value);
        if (isNaN(guess) || guess < 1 || guess > 100) {
            message.textContent = 'Por favor, ingresa un número válido entre 1 y 100.';
            return;
        }

        fetch('/guess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ guess: guess }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.result === 'mayor') {
                message.textContent = 'El número secreto es mayor. ¡Intenta de nuevo!';
            } else if (data.result === 'menor') {
                message.textContent = 'El número secreto es menor. ¡Intenta de nuevo!';
            } else if (data.result === 'correcto') {
                message.textContent = '¡Felicidades! ¡Has adivinado el número secreto!';
                gameOver = true;
                resetButton.style.display = 'inline-block';
            }
            attempts.textContent = `Intentos: ${data.attempts}`;
        })
        .catch(error => {
            console.error('Error:', error);
            message.textContent = 'Ocurrió un error. Por favor, intenta de nuevo.';
        });

        guessInput.value = '';
    }

    function resetGame() {
        fetch('/reset', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            message.textContent = 'Nuevo juego iniciado. ¡Adivina el número!';
            attempts.textContent = '';
            gameOver = false;
            resetButton.style.display = 'none';
        })
        .catch(error => {
            console.error('Error:', error);
            message.textContent = 'Error al reiniciar el juego. Por favor, recarga la página.';
        });
    }
});