from fastapi import FastAPI # importamos el API
from pydantic import BaseModel
from typing import List
import joblib # importamos la librería para cargar el modelo

class ApiInput(BaseModel):
    texts: List[str]

class ApiOutput(BaseModel):
    is_hate: List[int]

app = FastAPI() # creamos el api
model = joblib.load("model.joblib") # cargamos el modelo.

@app.post("/fake") # creamos api que permita requests de tipo post.
async def define_sentiment(data: ApiInput) -> ApiOutput:
    predictions = model.predict(data.texts).flatten().tolist() # generamos la predicción
    preds = ApiOutput(is_fake=predictions) # estructuramos la salida del API.
    return preds # retornamos los resultados
