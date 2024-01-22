import json
from sklearn.ensemble import IsolationForest

class DetectionModels:
    def __init__(self, model_config_path=None):
        if model_config_path is not None:
            with open(model_config_path) as w:
                self.model_def = json.load(w)

    
    def create_model(self, model_name=None, params=None):
        '''
        instantiate the model based on parameter and model name information
        '''
        if model_name is None and params is None:
            return None
        if model_name == 'IsolationForest' and params is not None:
            '''
            isolation forest is an ensemble machine learning algorithm used for anomaly detection.
            used in this method as the model to detect the outliers. 
            '''
            return IsolationForest(**params)
    

    def get_models(self):
        '''
        bring all the previous methods that returns 
        a list of all models defined in the appropriate config file
        '''
        models = []
        for model_definition in self.model_def:
            defined_model = self.create_model(model_name=model_definition['model'],
                                              params=model_definition['params']
                                              )
            models.append(defined_model)
        return models