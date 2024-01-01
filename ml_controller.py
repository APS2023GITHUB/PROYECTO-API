from fastapi import APIRouter, HTTPException, status
from models import Prediction_Input
from models import Prediction_Output
from models import Prediction_delete
import pickle


#cargar el modelo ml
#model=pickle.load(open('ml_model_reg_1.pkl', 'rb'))
model = pickle.load(open('ml_model_reg_1.pkl', 'rb'))
router=APIRouter()

preds=[]

@router.get('/ml')
def get_preds():
    return preds

@router.post('/ml', status_code=status.HTTP_201_CREATED, response_model=Prediction_Output)
def post_preds(pred_input: Prediction_Input):
     prediction_f = model.predict(([[pred_input.num_cuartos]]))
     prediction_dict = {"id": str(pred_input.id), "num_cuartos":str(pred_input.num_cuartos) , "precio_pred": float(prediction_f[0])}
     preds.append(prediction_dict)
     return prediction_dict

@router.delete('/ml/', status_code=202)
def delete_pred(pred_id:Prediction_delete):
    print(pred_id.id) 
    for pred_item in preds: 
        print(pred_item["id"])
        if int(pred_item["id"]) == int(pred_id.id):
            preds.remove(pred_item)
            return {'borrado correctamente'}
    else:
        raise HTTPException(status_code=404, detail='id no encontrado')