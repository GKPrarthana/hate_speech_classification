import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#project_name = "hate_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"hate/__init__.py",
    f"hate/components/__init__.py",
    f"hate/configuration/__init__.py",
    f"hate/constants/__init__.py",
    f"hate/entity/__init__.py",
    f"shate/exception/__init__.py",
    f"hate/logger/__init__.py",
    f"hate/ml/__init__.py",
    f"hate/pipeline/__init__.py",
    
    "app.py",
    "demo.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    else:
            logging.info(f"{filename} is already exists")