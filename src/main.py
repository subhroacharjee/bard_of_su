from fastapi import FastAPI
from src.models.palm_model import PalmAiModelSingleton
from typing import Optional, Union
from pydantic import BaseModel

palmModel = PalmAiModelSingleton()
app = FastAPI()

class InputPayload(BaseModel):
    msg: str

    temp: Optional[float]
    max_op_token: Optional[float]
    top_p: Optional[float] 
    top_k: Optional[float]


@app.post("/message")
def handle_message(input: InputPayload):
    # print(input)
    message = palmModel.message(msg=input.msg, temp=input.temp, max_op_token=input.max_op_token, top_k=input.top_k, top_p=input.top_p)
    return {
        "message": message
	}

@app.get('/')
def home_page():
    return {
        "resource": "is being deployed!"
    }