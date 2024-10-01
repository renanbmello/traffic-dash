# src/models/__init__.py

from .model import TrafficViolationDetector
from .utils import load_model, save_model

__all__ = [
    'TrafficViolationDetector',
    'load_model',
    'save_model',
]
