import joblib

from pydantic import BaseModel
from fastapi import FastAPI

##################################################################################

goalkeeper_model = joblib.load('Model/goalkeeper_logistic_model.joblib')
goalkeeper_scaler = joblib.load('Scaler/goalkeeper_logistic_scaler.joblib')

defender_model = joblib.load('Model/defender_logistic_model.joblib')
defender_scaler = joblib.load('Scaler/defender_logistic_scaler.joblib')

midfield_model = joblib.load('Model/midfield_logistic_model.joblib')
midfield_scaler = joblib.load('Scaler/midfield_logistic_scaler.joblib')

attack_model = joblib.load('Model/attack_logistic_model.joblib')
attack_scaler = joblib.load('Scaler/attack_logistic_scaler.joblib')

##################################################################################

class InputFeatures_goalkeeper(BaseModel):
    height: float
    appearance: int
    clean_sheets: float
    minutes_played: int
    games_injured: int
    award: int
    highest_value: int

class InputFeatures_defender(BaseModel):
    height: float
    appearance: int
    minutes_played: int
    games_injured: int
    award: int
    highest_value: int

class InputFeatures_midfield(BaseModel):
    height: float
    appearance: int
    goals: float
    assists: float
    minutes_played: int
    games_injured: int
    award: int
    highest_value: int

class InputFeatures_attack(BaseModel):
    appearance: int
    goals: float
    assists: float
    minutes_played: int
    games_injured: int
    award: int
    highest_value: int

##################################################################################

def preprocessing_goalkeeper(input_features: InputFeatures_goalkeeper):
    dict_f = {
        'height': input_features.height,
        'appearance': input_features.appearance,
        'clean sheets': input_features.clean_sheets,
        'minutes played': input_features.minutes_played,
        'games_injured': input_features.games_injured,
        'award': input_features.award,
        'highest_value': input_features.highest_value,
    }

    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]

    # Scale the input features
    scaled_features = goalkeeper_scaler.transform([list(dict_f.values())])

    return scaled_features

def preprocessing_defender(input_features: InputFeatures_defender):
    dict_f = {
        'height': input_features.height,
        'appearance': input_features.appearance,
        'minutes played': input_features.minutes_played,
        'games_injured': input_features.games_injured,
        'award': input_features.award,
        'highest_value': input_features.highest_value,
    }

    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]

    # Scale the input features
    scaled_features = defender_scaler.transform([list(dict_f.values())])

    return scaled_features

def preprocessing_midfield(input_features: InputFeatures_midfield):
    dict_f = {
        'height': input_features.height,
        'appearance': input_features.appearance,
        'goals': input_features.goals,
        'assists': input_features.assists,
        'minutes played': input_features.minutes_played,
        'games_injured': input_features.games_injured,
        'award': input_features.award,
        'highest_value': input_features.highest_value,
    }

    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]

    # Scale the input features
    scaled_features = midfield_scaler.transform([list(dict_f.values())])

    return scaled_features

def preprocessing_attack(input_features: InputFeatures_attack):
    dict_f = {
        'appearance': input_features.appearance,
        'goals': input_features.goals,
        'assists': input_features.assists,
        'minutes played': input_features.minutes_played,
        'games_injured': input_features.games_injured,
        'award': input_features.award,
        'highest_value': input_features.highest_value,
    }

    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]

    # Scale the input features
    scaled_features = attack_scaler.transform([list(dict_f.values())])

    return scaled_features

##################################################################################

app = FastAPI()

# GET request
@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}

@app.post("/goalkeeper/predict")
async def goalkeeper_predict(input_features: InputFeatures_goalkeeper):
    data = preprocessing_goalkeeper(input_features)
    print(2)
    y_pred = goalkeeper_model.predict(data)
    print(3)
    return {"pred": y_pred.tolist()[0]}

@app.post("/defender/predict")
async def defender_predict(input_features: InputFeatures_defender):
    data = preprocessing_defender(input_features)
    y_pred = defender_model.predict(data)
    return {"pred": y_pred.tolist()[0]}

@app.post("/midfield/predict")
async def midfield_predict(input_features: InputFeatures_midfield):
    data = preprocessing_midfield(input_features)
    y_pred = midfield_model.predict(data)
    return {"pred": y_pred.tolist()[0]}

@app.post("/attack/predict")
async def attack_predict(input_features: InputFeatures_attack):
    data = preprocessing_attack(input_features)
    y_pred = attack_model.predict(data)
    return {"pred": y_pred.tolist()[0]}
