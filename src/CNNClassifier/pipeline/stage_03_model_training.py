from CNNClassifier import logger
from CNNClassifier.config.configuration import ConfigurationManager2
from CNNClassifier.components.Training_Model import TrainingModel

STAGE_NAME="Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
           
           config=ConfigurationManager2()
           training_config=config.get_training_config()
           model_training=TrainingModel(config=training_config)
           logger.info("Selected Model for training")
           model_training.get_base_model()
           logger.info(f"Model Training started")
           model_training.train_valid_generator()
           model_training.train()
           logger.info("Model Trained successfully")

        except Exception as e:
            logger.info(f"Model Training failed")
            raise e
        
if __name__=="__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} started")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
        