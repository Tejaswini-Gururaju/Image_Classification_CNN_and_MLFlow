from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.Data_ingestion import DataIngestion
from CNNClassifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

# pipeline of all the entities and components

    def main(self):
        try:

           config=ConfigurationManager()
           data_ingestion_config=config.get_data_ingestion_config()
           data_ingestion=DataIngestion(config=data_ingestion_config)
           data_ingestion.download_data()
           data_ingestion.extract_zipfile()
        except Exception as e:
           raise e
        
if __name__=="__main__":
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e


