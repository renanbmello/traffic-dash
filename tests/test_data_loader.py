# tests/test_data_loader.py

import unittest
from src.data.data_loader import carregar_video

class TestDataLoader(unittest.TestCase):
    def test_carregar_video(self):
        video_path = 'data/raw/videos/exemplo.mp4'
        cap = carregar_video(video_path)
        self.assertIsNotNone(cap)

if __name__ == '__main__':
    unittest.main()
