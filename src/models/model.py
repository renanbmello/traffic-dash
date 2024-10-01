# src/models/model.py

from ultralytics import YOLO
import torch

class TrafficViolationDetector:
    def __init__(self, model_path: str = 'models/yolov8/yolov8n.pt'):
        """
        Inicializa o detector de infrações de trânsito.

        Args:
            model_path (str): Caminho para o modelo YOLOv8.
        """
        self.model = YOLO(model_path)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model.to(self.device)

    def detect(self, frame):
        """
        Realiza a detecção em um frame.

        Args:
            frame (np.ndarray): Frame de imagem.

        Returns:
            List[Dict]: Lista de detecções com informações de bounding boxes e classes.
        """
        results = self.model(frame)
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                class_name = self.model.names[class_id]
                detections.append({
                    'bbox': [x1, y1, x2, y2],
                    'confidence': confidence,
                    'class_id': class_id,
                    'class_name': class_name
                })
        return detections
