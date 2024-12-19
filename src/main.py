

from fastapi import FastAPI # importamos el API
from pydantic import BaseModel
from typing import List
import os
import joblib # importamos la librería para cargar el modelo

class ApiInput(BaseModel):
    texts: List[str]

class ApiOutput(BaseModel):
    is_fake: List[int]

app = FastAPI() # creamos el api
model = joblib.load("model.joblib") # cargamos el modelo.
vectorizer = joblib.load("vectorizer.joblib")


@app.post("/fake") # creamos api que permita requests de tipo post.
async def define_sentiment(data: ApiInput) -> ApiOutput:
    # Convertir los textos en vectores
    text_vectors = vectorizer.transform(data.texts)
    predictions = model.predict(text_vectors).flatten().tolist() # generamos la predicción
    preds = ApiOutput(is_fake=predictions) # estructuramos la salida del API.
    return preds # retornamos los resultados

# Configuramos el puerto para Railway
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
