import os
import pandas as pd
from src.Wine_Quality_ML.config.configuration import *
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into train and test sets.
        train, test = train_test_split(data, train_size=0.80)

        # Save the train and test sets
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logging.info(train.shape)
        logging.info(test.shape)

        print(train.shape)
        print(test.shape)