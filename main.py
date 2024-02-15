from src.Wine_Quality_ML.pipeline.stage01_data_ingestion_pipeline import *
from src.Wine_Quality_ML.pipeline.stage02_data_validation_pipeline import *
from src.Wine_Quality_ML.pipeline.stage03_data_transformation_pipeline import *
from src.Wine_Quality_ML.pipeline.stage04_model_trainer_pipeline import *
# from src.Wine_Quality_ML.pipeline.stage05_model_evaluation import *
from src.Wine_Quality_ML.logger import logging

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_01 = "DATA INGESTION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_01} started<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>> {STAGE_NAME_01} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_02 = "DATA VALIDATION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_02} started<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f">>> {STAGE_NAME_02} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_03 = "DATA TRANSFORMATION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_03} started<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logging.info(f">>> {STAGE_NAME_03} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_04 = "MODEL TRAINER STAGE"
try:
    logging.info(f">>> {STAGE_NAME_04} started<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logging.info(f">>> {STAGE_NAME_04} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>