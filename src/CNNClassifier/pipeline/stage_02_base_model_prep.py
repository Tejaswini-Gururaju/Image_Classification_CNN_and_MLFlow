from src.CNNClassifier.config.configuration import ConfigurationManager1
from src.CNNClassifier.components.Base_Model_prep import PrepareBaseModel
from src.CNNClassifier import logger


STAGE_NAME = "Prepration of Base Model"

class BaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:

           config=ConfigurationManager1()
           base_model_config=config.get_prepare_base_model_config()
           prepare_base_model=PrepareBaseModel(config=base_model_config)
           prepare_base_model.get_base_model()
           prepare_base_model.update_base_model()
        except Exception as e:
           raise e
        
if __name__=="__main__":
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj=BaseModelTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed successfully")

    except Exception as e:
        logger.exception(e)
        raise e


 
