from flask import Flask, render_template, request, jsonify
import requests
import numpy as np

app = Flask(__name__)

def calcular_densidade_superficial(payload):
    # Supondo que o payload seja um dicionário contendo as informações relevantes
    potencia_total = sum([ponto['flux'] for ponto in payload['data_points']])
    raio = payload['raio']

    # Calcula a densidade superficial de fluxo usando a equação fornecida
    densidade_superficial = potencia_total / (4 * np.pi * raio**2)
    
    return densidade_superficial

@app.route('/')
def index():
    return render_template('index.php')

@app.route('/analyze', methods=['POST'])
def analyze():
    payload = request.json['payload']
    
    # Chamada para a API do James Webb
    response = requests.get('http://localhost:5001/data')
    if response.status_code == 200:
        data = response.json()
        # Processamento do payload
        densidade_superficial = calcular_densidade_superficial(payload)
        data['densidade_superficial'] = densidade_superficial
        return jsonify(data)
    else:
        return jsonify({'error': 'Falha ao obter dados da API do James Webb'}), 500

if __name__ == '__main__':
    app.run(debug=True)
