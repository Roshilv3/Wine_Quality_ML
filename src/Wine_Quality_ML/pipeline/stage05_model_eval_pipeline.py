from src.Wine_Quality_ML.config.configuration import *
from src.Wine_Quality_ML.components.Model_Evaluation import *


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config= model_eval_config)
        model_eval.save_results()