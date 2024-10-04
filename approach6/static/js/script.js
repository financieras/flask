document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('diceForm');
  const resultadoElement = document.getElementById('resultado');

  form.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const formData = new FormData(form);
      
      fetch('/', {
          method: 'POST',
          body: formData
      })
      .then(response => response.json())
      .then(data => {
          resultadoElement.innerHTML = `El resultado es: ${data.resultado}`;
      })
      .catch(error => {
          console.error('Error:', error);
          resultadoElement.innerHTML = 'Hubo un error al lanzar el dado.';
      });
  });
});