// script.js
document.getElementById('analyzeButton').addEventListener('click', function() {
    var payload = document.getElementById('payloadInput').value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ payload: JSON.parse(payload) }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('infravermelhoConsole').textContent = data.infravermelho;
        document.getElementById('opticoConsole').textContent = data.optico;
        document.getElementById('regrasConsole').textContent = data.regras;
        document.getElementById('equacaoConsole').textContent = data.equacao;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
