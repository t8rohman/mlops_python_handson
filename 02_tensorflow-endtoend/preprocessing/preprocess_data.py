import numpy as np
import joblib

def preprocess_data(json_data:dict,
                    model_ver):
    
    try:
        pclass = json_data.get('Pclass', None)
        sex = json_data.get('Sex', None)
        age = json_data.get('Age', None)
        sibsp = json_data.get('SibSp', None)
        parch = json_data.get('Parch', None)
        fare = json_data.get('Fare', None)
        embarked = json_data.get('Embarked', None)

    except ValueError as e:
        print('One of the variables are missing, please check the data again!')

    cats = [pclass, sex, embarked]
    nums = [age, sibsp, parch, fare]

    encoder = joblib.load(f'preprocessing/encoder_{model_ver}/encoder.joblib')
    encoded_features = encoder.transform([cats])

    x = np.concatenate([nums, encoded_features[0]])
    x = x.reshape(1, -1)  # reshape the x feature to make it able to be passed to the tf model

    return x