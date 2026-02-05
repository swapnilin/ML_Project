# #Makefile defines named commands so developers don’t have to remember long, error-prone shell commands. Common uses:
# make setup        # env + deps
# make test         # unit tests
# make lint         # style checks
# make format       # auto-format
# make train        # run training
# make inference    # run predictions
# make clean        # remove temp files


.PHONY: setup lint test format run

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

lint:
	black src tests
	ruff src tests

test:
	pytest tests -v

format:
	black src tests

run:
	python src/flight_analytics/pipelines/train_pipeline.py
