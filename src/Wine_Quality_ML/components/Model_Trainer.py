import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from src.Wine_Quality_ML.config.configuration import *
from sklearn.linear_model import ElasticNet



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.test_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # reshaping y
        train_y = np.ravel(train_y)
        test_y = np.ravel(test_y)

        EN = ElasticNet(alpha= self.config.alpha,
                       l1_ratio= self.config.l1_ration,
                       random_state= 42
                      )
        # rf = RandomForestRegressor(criterion= self.config.criterion,
        #                            n_estimators= self.config.n_estimators,
        #                            max_depth= self.config.max_depth,
        #                            min_samples_leaf= self.config.min_samples_leaf)
        EN.fit(train_x, train_y)

        joblib.dump(EN, os.path.join(self.config.root_dir, self.config.model_name))