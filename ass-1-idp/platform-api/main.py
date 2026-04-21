from fastapi import FastAPI
from pydantic import BaseModel
from deployer import deploy_app

app = FastAPI()

class DeployRequest(BaseModel):
    app_name: str
    docker_image: str
    environment: str

@app.get("/")
def home():
    return {"message": "Internal Developer Platform API is running"}

@app.post("/deploy")
def deploy(request: DeployRequest):
    response = deploy_app(
        request.app_name,
        request.docker_image,
        request.environment
    )
    return response