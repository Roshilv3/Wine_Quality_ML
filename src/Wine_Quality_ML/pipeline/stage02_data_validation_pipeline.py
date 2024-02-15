from src.Wine_Quality_ML.config.configuration import *
from src.Wine_Quality_ML.components.Data_Validation import *


class DataValidationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validationl_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_columns()