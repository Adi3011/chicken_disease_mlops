from dataclasses import dataclass # dataclass decorator is used to create a class with attributes and methods
from pathlib import Path

@dataclass(frozen=True) # frozen=True makes the class immutable
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True) # frozen=True makes the class immutable
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classess: int    
    
@dataclass(frozen=True) # frozen=True makes the class immutable
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path    
    
    
@dataclass(frozen=True) # frozen=True makes the class immutable
class ModelTrainerConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list    