<!DOCTYPE html>
<html>
<head>
    <title>Análise Astronômica</title>
    <style>
        body {
            background-color: black;
            color: red;
            font-family: Arial, sans-serif;
        }
        .console {
            background-color: black;
            color: red;
            padding: 10px;
            border: 1px solid red;
            width: 80%;
            margin: 20px auto;
            overflow-y: scroll;
            height: 200px;
        }
        textarea {
            width: 80%;
            height: 100px;
            margin: 20px auto;
            display: block;
        }
        button {
            background-color: red;
            color: black;
            padding: 10px;
            margin-top: 10px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <textarea id="payloadInput" placeholder="Cole o payload aqui..."></textarea>
    <button id="analyzeButton">Analisar</button>
    <div class="console" id="console"></div>

    <script>
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
                document.getElementById('console').innerText = JSON.stringify(data, null, 4);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>


