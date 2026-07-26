import json
import os
import joblib
import pandas as pd
model=None

def init():
 global model
 model=joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"),"student_model.pkl"))

def run(raw_data):
 data=json.loads(raw_data)
 df=pd.DataFrame([data])
 p=model.predict(df)
 return {"PredictedScore":float(p[0])}
