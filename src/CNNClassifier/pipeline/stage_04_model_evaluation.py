from CNNClassifier import logger
from CNNClassifier.config.configuration import ConfigurationManager3
from CNNClassifier.components.Evaluation_with_mlflow import Evaluation

STAGE_NAME="Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager3()
            eval_config = config.get_evaluation_config()
            logger.info("Selected Model for Evaluation")
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            logger.info("Model Evaluation Completed and Logging into MLFlow started")
            evaluation.log_into_mlflow()
            logger.info("Experiment logged into mlflow")


        except Exception as e:
           logger.info(f"Model Evaluation Failed")
           raise e
        
if __name__=="__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} started")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
        