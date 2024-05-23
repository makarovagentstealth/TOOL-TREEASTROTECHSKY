import numpy as np

def calcular_densidade_superficial_fluxo(data):
    # Calcula a densidade superficial de fluxo usando a equação fornecida
    def calcular_densidade_superficial(potencia, raio):
        return potencia / (4 * np.pi * raio**2)

    # Supondo que a potência seja a soma dos fluxos de todos os pontos de dados
    potencia = sum([point['flux'] for point in data['data_points']])
    raio = data['raio']

    densidade_superficial = calcular_densidade_superficial(potencia, raio)
    
    return f"Densidade Superficial de Fluxo: {densidade_superficial}"
