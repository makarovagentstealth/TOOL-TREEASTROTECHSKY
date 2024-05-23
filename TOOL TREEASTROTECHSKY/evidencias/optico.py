# optico.py
import numpy as np

def process_optico(data):
    # Simulação de processamento usando Fotometria Diferencial
    def differential_photometry(data):
        # Exemplo de aplicação da técnica de fotometria diferencial
        mean_intensity = np.mean(data)
        diff_data = data - mean_intensity
        return diff_data
    
    fluxes = [point['flux'] for point in data['data_points']]
    processed_data = differential_photometry(np.array(fluxes))
    return f"Processado Óptico com Fotometria Diferencial: {processed_data}"
