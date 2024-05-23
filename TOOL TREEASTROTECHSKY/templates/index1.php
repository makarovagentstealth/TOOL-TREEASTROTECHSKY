<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
    <title>Resultados da Análise</title>
    <style>
        body { background-color: black; color: red; font-family: Arial, sans-serif; }
        .result { margin: 20px; }
        textarea { width: 100%; height: 100px; }
        button { background-color: red; color: black; padding: 10px; margin-top: 10px; }
        pre { background-color: black; color: red; padding: 10px; border: 1px solid red; }
    </style>
</head>
<body>
    <div class="result">
        <h1>Inserir Payload</h1>
        <textarea id="payloadInput"></textarea>
        <label for="raioInput">Raio do Círculo:</label>
        <input type="text" id="raioInput" placeholder="Informe o raio do círculo">
        <button id="analyzeButton">Analisar</button>
    </div>
    <div class="result">
        <h1>Infravermelho</h1>
        <pre id="infravermelhoConsole"></pre>
    </div>
    <div class="result">
        <h1>Óptico</h1>
        <pre id="opticoConsole"></pre>
    </div>
    <div class="result">
        <h1>Regras Aplicadas</h1>
        <pre id="regrasConsole"></pre>
    </div>
    <script src="/static/script.js"></script>
</body>
</html>
