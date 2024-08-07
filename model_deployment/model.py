import numpy as np
import joblib


model = joblib.load('../fraud_detection_xgboost_model.joblib')

def prediction(provider_id, product_id, category, channel_id, amount, pricing_strategy):
    prediction = model.predict(np.array([[provider_id, product_id, category, channel_id, amount, pricing_strategy]]))
    return prediction
