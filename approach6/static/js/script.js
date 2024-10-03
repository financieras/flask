fetch('/')
  .then(response => response.json())
  .then(data => {
    const resultadoElement = document.getElementById('resultado');
    resultadoElement.textContent = `El resultado es: ${data.resultado}`;
  });