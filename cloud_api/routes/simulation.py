# simulation.py
"""
API routes for ray simulation requests.
"""
from fastapi import APIRouter, HTTPException
from cloud_api.services.ray_tracing import run_ray_simulation

router = APIRouter()

@router.post("/rays")
def simulate_rays(num_rays: int, detector_distance: float):
    """Handles ray-tracing simulation requests."""
    if num_rays <= 0 or detector_distance <= 0:
        raise HTTPException(status_code=400, detail="num_rays and detector_distance must be positive values.")
    
    simulation_result = run_ray_simulation(num_rays, detector_distance)
    return simulation_result

