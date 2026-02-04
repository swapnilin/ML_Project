### Steps to follow:
Create a virtual environment
```bash
conda create -n project python=3.10 -y
```
-y automatically answers “yes” to confirmation prompts and -n is for the name of the environment.

After the env is created, switch to the new environment
```bash
conda activate project
```
Remember to delete environements after projects are completed. They take up lot of space in your drive.

Next, install all the modules required for this project using the requirements.txt file
```bash
pip install -r requirements.txt
```
When you start your project you may not know all the modules required upfront, you create this list just before the final commit using
```bash
pip freeze > requirements.txt
```
This captures exact versions and ensures anyone can reproduce your environment.


Note:
Notebooks are excluded from CI
src/ is linted, tested, deployed
Notebooks are for humans
src/ is for machines


```text
flight-analytics/
│
├── README.md
├── pyproject.toml          # or setup.py (build, deps, tooling)
├── Makefile                # common commands
├── .gitignore
├── .pre-commit-config.yaml
│
├── notebooks/              # HUMAN thinking space (not prod)
│   ├── 01_eda_initial.ipynb
│   ├── 02_feature_analysis.ipynb
│   └── 99_scratchpad.ipynb
│
├── configs/                # YAML-based configuration
│   ├── dev.yaml
│   ├── prod.yaml
│   └── features.yaml
│
├── src/                    # ALL production code
│   └── flight_analytics/
│       ├── __init__.py
│       │
│       ├── ingestion/
│       │   ├── load_raw.py
│       │   └── schemas.py
│       │
│       ├── preprocessing/
│       │   ├── clean.py
│       │   ├── validate.py
│       │   └── outliers.py
│       │
│       ├── features/
│       │   ├── build_features.py
│       │   └── feature_defs.py
│       │
│       ├── models/
│       │   ├── train.py
│       │   ├── predict.py
│       │   └── registry.py
│       │
│       ├── evaluation/
│       │   └── metrics.py
│       │
│       ├── pipelines/
│       │   ├── train_pipeline.py
│       │   └── inference_pipeline.py
│       │
│       └── utils/
│           ├── logging.py
│           └── io.py
│
├── tests/                  # ONLY tests, no logic
│   ├── unit/
│   │   ├── test_clean.py
│   │   └── test_features.py
│   └── integration/
│       └── test_pipeline.py
│
├── data_contracts/         # expectations, schemas
│   ├── raw_data.yaml
│   └── processed_data.yaml
│
├── sql/                    # warehouse logic
│   ├── sampling.sql
│   └── aggregations.sql
│
├── scripts/                # one-off operational jobs
│   └── backfill.py
│
└── .github/
    └── workflows/
        └── ci.yaml
```


