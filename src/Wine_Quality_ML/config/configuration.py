from src.Wine_Quality_ML.entity import *
from src.Wine_Quality_ML.utils import *
from src.Wine_Quality_ML.constants import *
from src.Wine_Quality_ML.logger import logging


class ConfigurationManager:
    def __init__(
            self,
            config_path = Config_File_Path,
            params_path = Params_File_Path,
            schema_path = Schema_File_Path
            ):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        self.schema = read_yaml(schema_path)

        create_directories([self.config.artifacts_root])

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
            )

        return data_ingestion_config
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def get_data_validationl_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.Columns

        create_directories([config.root_dir])

        data_validataion_config = DataValidationConfig(
            root_dir= config.root_dir,
            unzip_data_dir= config.unzip_data_dir,
            STATUS_FILE= config.STATUS_FILE,
            all_schema = schema
        )

        return data_validataion_config
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])


        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path
        )

        return data_transformation_config
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.Target_Column
        
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            alpha= params.alpha,
            l1_ration= params.l1_ration,
            target_column= schema.name
        )

        return model_trainer_config
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.Target_Column
        
        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            test_data_path= config.test_data_path,
            model_path= config.model_path,
            metrics_file_path= config.metrics_file_path,
            all_params= params,
            target_column= schema.name
        )

        return model_evaluation_config