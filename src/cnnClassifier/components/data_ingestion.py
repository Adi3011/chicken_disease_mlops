import os
import zipfile
import urllib.request as request
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import *
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
                )
            logger.info(f"{filename} downloaded successfully with following info: {headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists of size {get_size(Path(self.config.local_data_file))}")  
            
            
    def extract_zip_file(self):
        """
        zip_file_path: str
        extracts the zip file into the data directory
        function returns None
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        