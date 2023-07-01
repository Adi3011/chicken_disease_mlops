import os 
from pathlib import Path 
import logging 


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name ='cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",  #.gitkeep file is created to keep the folder in git
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    
]

for filepath in list_of_files:
    filepath = Path(filepath) #convert string to path object(forward and backward slash)
    filedir, filename = os.path.split(filepath) #split the path into directory and filename
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #create directory if it does not exist
        logging.info(f"Created directory at {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created file at {filepath}")
            
    else:
        logging.warning(f"File already exists at {filepath}")    