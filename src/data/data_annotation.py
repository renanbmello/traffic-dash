# src/data/data_annotation.py

import os
from typing import List, Dict
import json

def salvar_anotacoes(annotations: List[Dict], output_file: str):
    """
    Salva anotações em um arquivo JSON.

    Args:
        annotations (List[Dict]): Lista de anotações.
        output_file (str): Caminho para o arquivo de saída.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(annotations, f, indent=4)

def carregar_anotacoes(input_file: str) -> List[Dict]:
    """
    Carrega anotações de um arquivo JSON.

    Args:
        input_file (str): Caminho para o arquivo de entrada.

    Returns:
        List[Dict]: Lista de anotações.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"O arquivo de anotações {input_file} não foi encontrado.")
    with open(input_file, 'r') as f:
        annotations = json.load(f)
    return annotations
