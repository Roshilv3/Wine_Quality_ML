import os
import pandas as pd
import numpy as np
from pathlib import Path
import joblib

from src.Wine_Quality_ML.config.configuration import *
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config


    def metrics_eval(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        predicted_qualities = model.predict(test_x)

        (rmse, mae, r2) = self.metrics_eval(test_y, predicted_qualities)
        
        # Saving metrics as local
        scores = {"Root Mean Squared Error"  : rmse, 
                  "Mean Absoulte Error"      : mae, 
                  "r2_score"                 : r2
                  }
        save_json(path= Path(self.config.metrics_file_path), data=scores)