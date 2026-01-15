alembic revision --autogenerate -m "prestart script"
alembic upgrade head
uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload