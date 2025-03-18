# models.py
"""
API routes to list and load AI models.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/list")
def list_models():
    """Returns a list of available AI models."""
    return {"models": ["denoising_model", "inpainting_model"]}

@router.get("/load/{model_name}")
def load_model(model_name: str):
    """Loads the specified AI model."""
    available_models = {"denoising_model": "Denoising Model Loaded",
                        "inpainting_model": "Inpainting Model Loaded"}
    
    if model_name in available_models:
        return {"message": available_models[model_name]}
    else:
        return {"error": "Model not found"}

