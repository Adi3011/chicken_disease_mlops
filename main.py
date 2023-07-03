from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Running Stage {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()        
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e    