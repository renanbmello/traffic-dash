# tests/test_model.py

import unittest
from src.models import TrafficViolationDetector
import cv2

class TestModel(unittest.TestCase):
    def test_model_loading(self):
        detector = TrafficViolationDetector()
        self.assertIsNotNone(detector.model)

    def test_detection(self):
        detector = TrafficViolationDetector()
        frame = cv2.imread('data/processed/frames/frame_000001.jpg')
        detections = detector.detect(frame)
        self.assertIsInstance(detections, list)

if __name__ == '__main__':
    unittest.main()
