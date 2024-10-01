# src/app.py

import cv2
from src.detection.violation_detection import ViolationDetector

def main():
    video_path = 'data/raw/videos/exemplo.mp4'
    cap = cv2.VideoCapture(video_path)
    violation_detector = ViolationDetector()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        infracoes = violation_detector.detectar_infracoes(frame)

        # Exibir infrações detectadas
        for infracao in infracoes:
            tipo = infracao['tipo']
            detalhes = infracao['detalhes']
            x1, y1, x2, y2 = detalhes['bbox']
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, tipo, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow('Detecção de Infrações', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
