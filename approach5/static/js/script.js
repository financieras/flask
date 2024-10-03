// script.js
const form = document.querySelector('form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', (event) => {
    event.preventDefault(); // Evita que se recargue la página

    const formData = new FormData(form);
    const numFaces = formData.get('num_faces');

    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.textContent = `El resultado es: ${data.result}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});