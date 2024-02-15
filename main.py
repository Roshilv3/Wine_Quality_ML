from src.Wine_Quality_ML.pipeline.stage01_data_ingestion_pipeline import *
# from src.Wine_Quality_ML.pipeline.stage02_data_validation import *
# from src.Wine_Quality_ML.pipeline.stage03_data_transformation import *
# from src.Wine_Quality_ML.pipeline.stage04_model_trainer import *
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

