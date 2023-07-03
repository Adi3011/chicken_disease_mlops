from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_basemodel import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from cnnClassifier.pipeline.stage_05_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Running Stage {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()        
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e    



STAGE_NAME = "Prepare Base Model Training Stage"
try:
    logger.info(f"Running Stage {STAGE_NAME}")
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()        
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e    

STAGE_NAME = "Prepare Model Training Stage"
try:
    logger.info(f"Running Stage {STAGE_NAME}")
    pipeline = ModelTrainerPipeline()
    pipeline.main()        
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e    

STAGE_NAME = "Evaluation Stage"
try:
    logger.info(f"Running Stage {STAGE_NAME}")
    pipeline = EvaluationPipeline()
    pipeline.main()        
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e    


