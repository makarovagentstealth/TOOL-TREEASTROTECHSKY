from evidencias.infravermelho import process_infravermelho
from equacoes.equacoes import calcular_equacao_geometrica

def run_infravermelho_module(data):
    processed_data = process_infravermelho(data)
    area_circulo = calcular_equacao_geometrica(data)
    return {
        'processed_data': processed_data,
        'area_circulo': area_circulo
    }
