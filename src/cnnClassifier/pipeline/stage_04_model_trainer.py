from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import ModelTrainer 
from cnnClassifier import logger
from cnnClassifier.components.prepare_callbacks import PrepareCallbacks
STAGE_NAME = "Prepare Base Model Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_model_trainer_config()
        training = ModelTrainer(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f"Running Stage {STAGE_NAME}")
        pipeline = ModelTrainerPipeline()
        pipeline.main()        
        logger.info(f"Stage {STAGE_NAME} completed successfully")
    except Exception as e:
        logger.exception(e)
        raise e    
    
    
    