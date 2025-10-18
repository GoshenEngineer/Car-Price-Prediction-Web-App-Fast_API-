import pickle
import pandas as pd
import pickle
import numpy as np
import joblib
from tensorflow.keras.models import load_model

#import the ml model
#Load the trained model
loaded_model = load_model('model/nn_model.keras')
#Load the trained scaler
scaler = joblib.load('model/scaler.joblib')
#Load the pipeline model
preprocessor = joblib.load('model/preprocessor.joblib')

#ML_FLOW
MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])          
    X = preprocessor.transform(df)
    num_cat_pre = X[:,:-1]
    model_pre = X[:,-1]
    
    #make prediction
    prediction = loaded_model.predict([num_cat_pre, model_pre])
    # Convert predictions back to original scale
    prediction = scaler.inverse_transform(prediction)
    prediction = float(prediction[0])

    #response
    return {
        "Selling Price": prediction
    }