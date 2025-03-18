# utils.py
"""
Helper utility functions for logging and data processing.
"""
import logging
import numpy as np

def setup_logger():
    """Sets up a logger for the application."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger("OpenRBYR-Cloud")

def normalize_image(image: np.ndarray):
    """Normalizes an image array to the range [0,1]."""
    return (image - image.min()) / (image.max() - image.min() + 1e-8)

def validate_projections(projections: list):
    """Ensures projection data is in the correct format before reconstruction."""
    projections = np.array(projections)
    if projections.ndim != 2:
        raise ValueError("Projections must be a 2D array.")
    return projections

