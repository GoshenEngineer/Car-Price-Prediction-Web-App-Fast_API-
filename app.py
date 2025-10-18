from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field, field_validator
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, loaded_model, MODEL_VERSION
import pandas as pd


app = FastAPI()

#human readability       
@app.get('/')
def home():
    return  {'message':'Car Price Prediction API'}

#machine readable
@app.get('/Car')
def Model_check():
    return {
        'status' : 'OK',
        'version':MODEL_VERSION,
        'model_loaded':loaded_model is not None
    }
@app.post('/predict')
def pred_premium(data: UserInput):


    user_input = {

        'brand':data.brand,
        'model':data.model,
        'vehicle_age': data.vehicle_age,
        'km_driven': data.km_driven,
        'seller_type': data.seller_type,
        'fuel_type':data.fuel_type,
        'transmission_type':data.transmission_type,
        'mileage':data.mileage,
        'engine':data.engine,
        'max_power':data.max_power,
        'seats':data.seats

    }

    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content = {'response':prediction})
    
    except Exception as e:

        return JSONResponse(status_code = 500, content=str(e))


                                                                                                                                      