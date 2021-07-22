import joblib
import numpy as np
import pandas as pd
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from app.app import *

app = FastAPI()


@app.get("/")
def hello():
    return {"message":"Hello Sherlock"}


@app.post('/predict')
async def predict(model_name: str, data: str):

    model = joblib.load('models/{}'.format(model_name))

    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
To cover:
- possible return types: not nympy array, etc
"""