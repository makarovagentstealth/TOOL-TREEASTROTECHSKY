from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/data')
def get_data():
    # URL da API real do James Webb
    url = 'https://www.jwst.nasa.gov/content/webbLaunch/whereIsWebb.html'

    # Fazendo uma requisição para a API
    response = requests.get(url)
    
    # Tratamento dos dados obtidos
    if response.status_code == 200:
        # Aqui estamos simulando o processamento do HTML da página
        # Você precisa adaptar esse processamento conforme a estrutura real da página
        infravermelho_data = 'dados_infravermelho'
        optico_data = 'dados_optico'
    else:
        infravermelho_data = 'dados_infravermelho'
        optico_data = 'dados_optico'

    # Estrutura de dados para a resposta da API
    result = {
        'infravermelho': infravermelho_data,
        'optico': optico_data
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
