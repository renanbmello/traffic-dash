# src/detection/plate_recognition.py

import cv2
import pytesseract

def reconhecer_placa(roi):
    """
    Reconhece o texto da placa em uma região de interesse.

    Args:
        roi (np.ndarray): Imagem da placa.

    Returns:
        str: Texto reconhecido na placa.
    """
    # Pré-processamento
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]

    # OCR
    config = '--psm 8 --oem 3'
    texto = pytesseract.image_to_string(thresh, config=config, lang='eng')
    return texto.strip()
