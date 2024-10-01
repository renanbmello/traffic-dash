# src/utils/image_utils.py

import cv2
import numpy as np

def redimensionar_imagem(image, width: int = None, height: int = None):
    """
    Redimensiona uma imagem mantendo a proporção.

    Args:
        image (np.ndarray): Imagem a ser redimensionada.
        width (int, optional): Largura desejada. Se None, calcula proporcionalmente.
        height (int, optional): Altura desejada. Se None, calcula proporcionalmente.

    Returns:
        np.ndarray: Imagem redimensionada.
    """
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        ratio = height / float(h)
        dimension = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        dimension = (width, int(h * ratio))
    resized = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
    return resized
