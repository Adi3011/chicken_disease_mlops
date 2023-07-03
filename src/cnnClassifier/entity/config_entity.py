from dataclasses import dataclass # dataclass decorator is used to create a class with attributes and methods
from pathlib import Path

@dataclass(frozen=True) # frozen=True makes the class immutable
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
    