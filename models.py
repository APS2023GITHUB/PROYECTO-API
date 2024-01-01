from pydantic import BaseModel

class Prediction_Input(BaseModel):
    id: int
    num_cuartos: int

class Prediction_Output(BaseModel):
    id: int
    num_cuartos: int
    precio_pred: float

class Prediction_delete(BaseModel):
    id: int