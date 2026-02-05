# create_faang_repo.py
import os
from pathlib import Path

# ------------------------------
# Project root name
# ------------------------------
project_name = "flight_analytics"

# ------------------------------
# List of files and folders to create
# ------------------------------
list_of_files = [
    # src structure
    f"{project_name}/src/{project_name}/__init__.py",
    
    f"{project_name}/src/{project_name}/ingestion/__init__.py",
    f"{project_name}/src/{project_name}/ingestion/load_raw.py",
    f"{project_name}/src/{project_name}/ingestion/schemas.py",

    f"{project_name}/src/{project_name}/preprocessing/__init__.py",
    f"{project_name}/src/{project_name}/preprocessing/clean.py",
    f"{project_name}/src/{project_name}/preprocessing/validate.py",
    f"{project_name}/src/{project_name}/preprocessing/outliers.py",

    f"{project_name}/src/{project_name}/features/__init__.py",
    f"{project_name}/src/{project_name}/features/build_features.py",
    f"{project_name}/src/{project_name}/features/feature_defs.py",

    f"{project_name}/src/{project_name}/models/__init__.py",
    f"{project_name}/src/{project_name}/models/train.py",
    f"{project_name}/src/{project_name}/models/predict.py",
    f"{project_name}/src/{project_name}/models/registry.py",

    f"{project_name}/src/{project_name}/evaluation/__init__.py",
    f"{project_name}/src/{project_name}/evaluation/metrics.py",

    f"{project_name}/src/{project_name}/pipelines/__init__.py",
    f"{project_name}/src/{project_name}/pipelines/train_pipeline.py",
    f"{project_name}/src/{project_name}/pipelines/inference_pipeline.py",

    # logging as top-level package
    f"{project_name}/src/{project_name}/logger/__init__.py",
    f"{project_name}/src/{project_name}/logger/logger.py",

    # exception as top-level package
    f"{project_name}/src/{project_name}/exception/__init__.py",
    f"{project_name}/src/{project_name}/exception/exception.py",

    # notebooks
    f"{project_name}/notebooks/01_eda.ipynb",
    f"{project_name}/notebooks/02_feature_testing.ipynb",
    f"{project_name}/notebooks/99_scratchpad.ipynb",

    # configs
    f"{project_name}/configs/dev.yaml",
    f"{project_name}/configs/prod.yaml",
    f"{project_name}/configs/features.yaml",

    # data contracts
    f"{project_name}/data_contracts/raw_data.yaml",
    f"{project_name}/data_contracts/processed_data.yaml",

    # SQL
    f"{project_name}/sql/sampling.sql",
    f"{project_name}/sql/aggregations.sql",

    # scripts
    f"{project_name}/scripts/backfill.py",

    # root files
    f"{project_name}/README.md",
    f"{project_name}/requirements.txt",
    f"{project_name}/Dockerfile",
    f"{project_name}/.dockerignore",
    f"{project_name}/setup.py",
    f"{project_name}/pyproject.toml",
    f"{project_name}/Makefile",
    f"{project_name}/.gitignore",
]

# ------------------------------
# Create folders and files
# ------------------------------
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # create folders
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    # create empty files if they don't exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            # optional: add placeholder content for .py files
            if filename.endswith(".py"):
                f.write(f"# {filename} - TODO: implement\n")
            elif filename.endswith(".ipynb"):
                f.write('{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}')
    else:
        print(f"File already exists: {filepath}")

print(f"\n✅ FAANG-style repo '{project_name}' scaffold created successfully!")
