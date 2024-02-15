from src.Wine_Quality_ML.config.configuration import *
from src.Wine_Quality_ML.components.Model_Trainer import *


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config= model_trainer_config)
        model_trainer.train()