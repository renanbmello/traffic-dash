# src/detection/signal_detection.py

import cv2
import numpy as np

def detectar_estado_semaforo(roi):
    """
    Determina o estado do semáforo em uma região de interesse.

    Args:
        roi (np.ndarray): Imagem do semáforo.

    Returns:
        str: Estado do semáforo ('vermelho', 'amarelo', 'verde' ou 'desconhecido').
    """
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # Definir limites para as cores
    # Vermelho
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Amarelo
    lower_yellow = np.array([15, 70, 50])
    upper_yellow = np.array([35, 255, 255])
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Verde
    lower_green = np.array([36, 70, 50])
    upper_green = np.array([89, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Verificar se há pixels suficientes em cada máscara
    if cv2.countNonZero(mask_red) > 50:
        return 'vermelho'
    elif cv2.countNonZero(mask_yellow) > 50:
        return 'amarelo'
    elif cv2.countNonZero(mask_green) > 50:
        return 'verde'
    else:
        return 'desconhecido'
