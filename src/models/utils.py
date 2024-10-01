# src/models/utils.py

import torch

def load_model(model_path: str):
    """
    Carrega um modelo treinado.

    Args:
        model_path (str): Caminho para o modelo salvo.

    Returns:
        torch.nn.Module: Modelo carregado.
    """
    model = torch.load(model_path)
    return model

def save_model(model, model_path: str):
    """
    Salva um modelo treinado.

    Args:
        model (torch.nn.Module): Modelo a ser salvo.
        model_path (str): Caminho para salvar o modelo.
    """
    torch.save(model, model_path)
