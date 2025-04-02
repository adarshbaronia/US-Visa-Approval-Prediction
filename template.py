import os
from pathlib import Path

project_name = "us_visa"

# Replace f-strings with string concatenation or .format()
list_of_files = [
    project_name + "/__init__.py",
    project_name + "/components/__init__.py",
    project_name + "/components/data_ingestion.py",  
    project_name + "/components/data_validation.py",
    project_name + "/components/data_transformation.py",
    project_name + "/components/model_trainer.py",
    project_name + "/components/model_evaluation.py",
    project_name + "/components/model_pusher.py",
    project_name + "/configuration/__init__.py",
    project_name + "/constants/__init__.py",
    project_name + "/entity/__init__.py",
    project_name + "/entity/config_entity.py",
    project_name + "/entity/artifact_entity.py",
    project_name + "/exception/__init__.py",
    project_name + "/logger/__init__.py",
    project_name + "/pipline/__init__.py",
    project_name + "/pipline/training_pipeline.py",
    project_name + "/pipline/prediction_pipeline.py",
    project_name + "/utils/__init__.py",
    project_name + "/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print("Created directory: " + filedir)
    
    # Check if file exists or is empty and create if necessary
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            # Optionally, add initial content
            if filename.endswith(".py"):
                f.write("# Python file for project\n")
            else:
                f.write("# Configuration file\n")
            print("Created file: " + str(filepath))
    else:
        print("File already exists: " + str(filepath))
