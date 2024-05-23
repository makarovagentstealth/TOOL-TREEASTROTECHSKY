from evidencias.optico import process_optico
from equacoes.equacoes import calcular_equacao_geometrica

def run_optico_module(data):
    processed_data = process_optico(data)
    area_circulo = calcular_equacao_geometrica(data)
    return {
        'processed_data': processed_data,
        'area_circulo': area_circulo
    }
