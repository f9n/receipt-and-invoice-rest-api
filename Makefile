
export-requirements:
	poetry export -f requirements.txt --output requirements.txt

run:
	poetry run uvicorn app.main:app --reload
