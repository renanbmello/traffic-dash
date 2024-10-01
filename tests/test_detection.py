# tests/test_detection.py

import unittest
from src.detection.violation_detection import ViolationDetector
import cv2

class TestDetection(unittest.TestCase):
    def test_violation_detection(self):
        detector = ViolationDetector()
        frame = cv2.imread('data/processed/frames/frame_000001.jpg')
        infracoes = detector.detectar_infracoes(frame)
        self.assertIsInstance(infracoes, list)

if __name__ == '__main__':
    unittest.main()
