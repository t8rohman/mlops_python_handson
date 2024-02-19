import os
import configparser
from flask import Flask, request, jsonify

import tensorflow as tf
import preprocessing.preprocess_data as preprocess

# read config file which has the model_version
config = configparser.ConfigParser()
config.read('config.cfg')

model_ver = config['model']['model_ver']

app = Flask(__name__)

model_path = f'model/v{model_ver}/'             # adjust this model_path based on the version
model = tf.keras.models.load_model(model_path)  # load the tensorflow formatted model using tf.keras.models


@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.json
    data = preprocess.preprocess_data(data, model_ver)   # preprocessing the data for the categorical cols
    prediction = model.predict(data)                     # make a prediction

    return jsonify({'predictions': prediction.tolist()})


if __name__ == '__main__':
    
    app.run(host="0.0.0.0",                          # flask app should listen on all available network interfaces, making it accessible from any network.
            port=int(os.environ.get("PORT", 8080))   # set port at 8080, default without specifying this will be located at port 5000
            )