import os

ROOT_DIR = os.path.dirname(__file__)                                        # __file__ is a built-in variable that represents the current script's file path. 
MODEL_CONFIG_PATH = os.path.join(ROOT_DIR, 'configs/model_config.json')     # pointing out to the file where it contains the model and it's parameters.