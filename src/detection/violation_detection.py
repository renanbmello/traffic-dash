# src/detection/violation_detection.py

from src.models import TrafficViolationDetector
from src.detection.signal_detection import detectar_estado_semaforo
from src.detection.lane_detection import detectar_faixas
from src.detection.plate_recognition import reconhecer_placa
import cv2

class ViolationDetector:
    def __init__(self, model_path='models/yolov8/yolov8n.pt'):
        self.detector = TrafficViolationDetector(model_path)

    def detectar_infracoes(self, frame, previous_frame=None):
        """
        Detecta infrações em um frame.

        Args:
            frame (np.ndarray): Frame atual.
            previous_frame (np.ndarray, optional): Frame anterior para análise de movimento.

        Returns:
            List[Dict]: Lista de infrações detectadas.
        """
        detections = self.detector.detect(frame)
        infracoes = []

        for det in detections:
            class_name = det['class_name']
            bbox = det['bbox']

            if class_name == 'traffic light':
                x1, y1, x2, y2 = bbox
                roi = frame[y1:y2, x1:x2]
                estado_semaforo = detectar_estado_semaforo(roi)
                if estado_semaforo == 'vermelho':
                    # Implementar lógica para verificar se um veículo avançou o sinal
                    infracao = {
                        'tipo': 'Avanço de sinal vermelho',
                        'detalhes': det
                    }
                    infracoes.append(infracao)

            elif class_name == 'car' or class_name == 'motorcycle':
                # Implementar lógica para outras infrações
                pass

        return infracoes
