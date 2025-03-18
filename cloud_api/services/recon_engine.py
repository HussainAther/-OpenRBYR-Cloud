# recon_engine.py
"""
Handles AI-based reconstruction processing.
"""
import numpy as np

def run_reconstruction(projections: list, num_iterations: int):
    """Performs AI-based iterative CT reconstruction."""
    projections = np.array(projections)
    reconstructed_image = np.ones_like(projections)
    
    for _ in range(num_iterations):
        reconstructed_image *= projections / (np.sum(reconstructed_image, axis=0) + 1e-8)  # Avoid division by zero
    
    return {"reconstructed_image": reconstructed_image.tolist()}

