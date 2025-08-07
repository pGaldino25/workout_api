run:
	@.venv/bin/python -m uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHON:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHON:$(pwd) alembic upgrade head

run-docker:
	@docker compose up -d

down-docker:
	@docker compose down
