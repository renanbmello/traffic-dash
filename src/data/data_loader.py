# src/data/data_loader.py

import cv2
import os
from typing import List

def carregar_video(video_path: str) -> cv2.VideoCapture:
    """
    Carrega um vídeo dado o caminho para o arquivo.

    Args:
        video_path (str): Caminho para o arquivo de vídeo.

    Returns:
        cv2.VideoCapture: Objeto de captura de vídeo.
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"O vídeo {video_path} não foi encontrado.")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Não foi possível abrir o vídeo {video_path}.")
    return cap

def extrair_frames(video_path: str, output_dir: str) -> List[str]:
    """
    Extrai frames de um vídeo e salva em um diretório.

    Args:
        video_path (str): Caminho para o arquivo de vídeo.
        output_dir (str): Diretório onde os frames serão salvos.

    Returns:
        List[str]: Lista de caminhos para os frames extraídos.
    """
    cap = carregar_video(video_path)
    os.makedirs(output_dir, exist_ok=True)
    frame_paths = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(output_dir, f"frame_{frame_count:06d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_paths.append(frame_filename)
        frame_count += 1

    cap.release()
    return frame_paths
