# ai_models.py
"""
Handles AI model loading and inference.
"""
import torch
import torch.nn as nn

class DenoisingModel(nn.Module):
    def __init__(self):
        super(DenoisingModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(16, 1, kernel_size=3, padding=1)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        return x


def load_model(model_name: str):
    """Loads the requested AI model."""
    if model_name == "denoising_model":
        model = DenoisingModel()
        model.load_state_dict(torch.load("models/denoising_model.pth"))
        model.eval()
        return model
    elif model_name == "inpainting_model":
        model = DenoisingModel()  # Placeholder for actual inpainting model
        model.load_state_dict(torch.load("models/inpainting_model.pth"))
        model.eval()
        return model
    else:
        raise ValueError("Model not found")

