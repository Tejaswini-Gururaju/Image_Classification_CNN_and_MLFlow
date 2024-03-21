from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from CNNClassifier.pipeline.stage_02_base_model_prep import BaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from CNNClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
import os

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/tejaswini1999teju15/Image_Classification_CNN_and_MLFlow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="tejaswini1999teju15"
os.environ["MLFLOW_TRACKING_PASSWORD"]="cc67f8b5467bbf2bf69794d3f1e8d40572f3b506"

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

STAGE_NAME = "Model Training"

try:
    logger.info(f"Stage {STAGE_NAME} started")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"

try:
    logger.info(f"Stage {STAGE_NAME} started")
    obj=ModelEvaluationPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
