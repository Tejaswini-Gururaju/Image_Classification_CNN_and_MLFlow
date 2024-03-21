import logging
import zipfile
import gdown
import os
from CNNClassifier import logger
from CNNClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_data(self) -> str:
        try:
            
            dataset_url = self.config.source_url
            zipfile_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} to {zipfile_dir}")
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zipfile_dir )
            logger.info(f"Data downloaded successfully")

        except Exception as e:
            logger.info("Data download failed {e}")
            raise e
        
    def extract_zipfile(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Data Extracted successfully from the Zip file")


        

    