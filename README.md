# OpenRBYR-Cloud: Cloud-Based CT Simulation & Reconstruction API 🚀

## 📌 Overview
**OpenRBYR-Cloud** is a scalable cloud-based API for remote execution of **ray-by-ray computed tomography (CT) simulations** and **AI-driven reconstruction**. Built with **FastAPI**, it provides a seamless interface for researchers, medical professionals, and developers to run advanced imaging computations without requiring local installations.

---

## 🚀 Features
- **Remote Ray-Tracing Simulations** – Execute ray-based CT models via API calls.
- **AI-Powered CT Reconstruction** – Perform GAN-based denoising and inpainting.
- **Scalable Cloud Deployment** – Runs on cloud platforms with containerized execution.
- **RESTful API with FastAPI** – Easily integrate with other applications.
- **Automated CI/CD Deployment** – GitHub Actions for testing & deployment.

---

## 🔧 Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YourGitHub/OpenRBYR-Cloud.git
cd OpenRBYR-Cloud
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the API Locally**
```bash
uvicorn cloud_api.api:app --reload --host 0.0.0.0 --port 8000
```

### **4️⃣ Test the API Endpoints**
Once running, visit `http://127.0.0.1:8000/docs` for an interactive API documentation (Swagger UI).

---

## 📂 Project Structure
```
OpenRBYR-Cloud/
│── cloud_api/              # Main API source code
│   │── __init__.py
│   │── api.py               # FastAPI server for remote execution
│   │── routes/
│       │── simulation.py     # Routes for ray simulation requests
│       │── reconstruction.py # Routes for reconstruction requests
│       │── models.py         # Routes for AI model inference
│   │── services/
│       │── ray_tracing.py    # Handles ray-tracing simulations
│       │── recon_engine.py   # Handles AI-based reconstruction
│       │── ai_models.py      # Loads and runs AI models
│   │── utils.py              # Helper functions
│
│── models/                  # Pre-trained AI models
│   │── denoising_model.pth
│   │── inpainting_model.pth
│
│── tests/                   # Unit tests
│   │── test_api.py
│   │── test_simulation.py
│   │── test_reconstruction.py
│
│── docs/                    # Documentation
│
│── .github/                 # GitHub automation & CI/CD
│   │── workflows/
│       │── tests.yml        # Runs automatic tests on commits
