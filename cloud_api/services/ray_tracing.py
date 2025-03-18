# ray_tracing.py
"""
Handles ray-tracing simulations.
"""
import numpy as np

def run_ray_simulation(num_rays: int, detector_distance: float):
    """Simulates ray tracing through a CT scanner setup."""
    rays = np.linspace(-detector_distance, detector_distance, num_rays)
    intensities = np.exp(-np.abs(rays) / detector_distance)  # Simple attenuation model
    return {"rays": rays.tolist(), "intensities": intensities.tolist()}

