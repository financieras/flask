const form = document.querySelector('form');
const resultadoElement = document.getElementById('resultado');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const numCaras = formData.get('num_caras');

  fetch('/')
    .then(response => response.json())
    .then(data => {
      resultadoElement.innerHTML = `El resultado es: ${data.resultado}`;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});