from src.CNNClassifier import logger
from src.CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.CNNClassifier.pipeline.stage_02_base_model_prep import BaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepration of Base Model"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj=BaseModelTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
