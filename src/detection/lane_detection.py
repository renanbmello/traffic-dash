# src/detection/lane_detection.py

import cv2
import numpy as np

def detectar_faixas(frame):
    """
    Detecta faixas na pista em um frame.

    Args:
        frame (np.ndarray): Frame de imagem.

    Returns:
        np.ndarray: Frame com as faixas desenhadas.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    # Definir região de interesse
    height = frame.shape[0]
    polygons = np.array([
        [(0, height), (frame.shape[1], height), (frame.shape[1], height//2), (0, height//2)]
    ])
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, polygons, 255)
    masked_edges = cv2.bitwise_and(edges, mask)

    # Detectar linhas usando a Transformada de Hough
    lines = cv2.HoughLinesP(
        masked_edges,
        rho=1,
        theta=np.pi/180,
        threshold=50,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=100
    )

    # Desenhar as linhas na imagem original
    line_image = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    return combo_image
