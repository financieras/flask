document.addEventListener('DOMContentLoaded', () => {
    const heightInput = document.getElementById('height');
    const widthInput = document.getElementById('width');
    const numPlayersInput = document.getElementById('num-players');
    const amountFoodInput = document.getElementById('amount-food');
    const foodValueDisplay = document.getElementById('food-value');
    const startBtn = document.getElementById('startBtn');
    const gameBoard = document.getElementById('game-board');

    amountFoodInput.addEventListener('input', () => {
        foodValueDisplay.textContent = `${amountFoodInput.value}%`;
    });

    startBtn.addEventListener('click', () => {
        const height = parseInt(heightInput.value);
        const width = parseInt(widthInput.value);
        const numPlayers = parseInt(numPlayersInput.value);
        const amountFood = parseInt(amountFoodInput.value);

        fetch('/start_game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                height: height, 
                width: width, 
                num_players: numPlayers, 
                amount_food: amountFood 
            }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Red no válida');
            }
            return response.json();
        })
        .then(data => {
            updateGameBoard(data.board);
        })
        .catch(error => {
            console.error('Error:', error);
            gameBoard.textContent = 'Ocurrió un error al iniciar el juego.';
        });
    });

    function updateGameBoard(board) {
        gameBoard.innerHTML = '';
        
        for (let row of board) {
            const rowElement = document.createElement('div');
            rowElement.className = 'game-row';
            for (let cell of row) {
                const cellElement = document.createElement('div');
                cellElement.className = 'game-cell';
                cellElement.textContent = getCellContent(cell);
                cellElement.style.backgroundColor = getCellColor(cell);
                rowElement.appendChild(cellElement);
            }
            gameBoard.appendChild(rowElement);
        }
    }

    function getCellColor(cell) {
        if (!isNaN(cell) && cell >= 1 && cell <= 9) return '#e6ffe6';  // Light green for food
        if (cell === '·') return 'white';  // Empty
        if ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.includes(cell)) return '#ffe6e6';  // Light red for players
        return 'gray';  // Unknown
    }

    function getCellContent(cell) {
        if (!isNaN(cell) && cell >= 1 && cell <= 9) return cell;  // Food
        if (cell === '·') return '';  // Empty
        if ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.includes(cell)) return cell;  // Players
        return '';  // Unknown
    }
});