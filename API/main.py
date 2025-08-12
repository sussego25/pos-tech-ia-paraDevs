from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
import pickle

from models.dengue_parametros import DengueFeatures
from services.previsao_dengue_service import PrevisaoDengueService

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return "Healthy"


@app.get("/previsao_dengue")
def predict(
    features: Annotated[DengueFeatures, Query(description="Dados para previsão se o pessoa tem dengue ou não de acordo com sintomas e ID do municipio.")]
):
    try:
        service = PrevisaoDengueService(model, features)
        return service.predict()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))