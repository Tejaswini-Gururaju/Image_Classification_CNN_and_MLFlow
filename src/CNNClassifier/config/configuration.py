from src.CNNClassifier.constants import *
from src.CNNClassifier.utils.common import read_yaml,create_directories
from src.CNNClassifier.entity.config_entity import DataIngestionConfig
from src.CNNClassifier.entity.config_entity import PrepareBaseModelConfig


class ConfigurationManager:
    # def __init__(self,config_file_path = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
    def __init__(self,config_file_path = CONFIG_FILE_PATH):

        self.config=read_yaml(config_file_path)
        self.params=read_yaml(Path("params.yaml"))

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config =DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir

        )

        return data_ingestion_config



class ConfigurationManager1:
    def __init__(self,
                #  config_filePath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(Path("config/config.yaml"))
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config=self.config.prepare_base_model
        params = self.params
        create_directories([config.root_dir])

        base_model_config=PrepareBaseModelConfig(
                root_dir = config.root_dir,
                base_model_path = config.base_model_path,
                updated_base_model_path = config.updated_base_model_path,
                params_image_size = params.IMAGE_SIZE,
                params_learning_rate = params.LEARNING_RATE,
                params_include_top = params.INCLUDE_TOP,
                params_weight = params.WEIGHTS,
                params_classes= params.CLASSES,
            
        )
        return base_model_config


    


