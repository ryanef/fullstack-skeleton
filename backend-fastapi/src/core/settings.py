import os
from dotenv import load_dotenv

load_dotenv()

PG_DB = os.environ['POSTGRES_DB']
PG_HOST = os.environ['POSTGRES_HOST']
PG_USER = os.environ['POSTGRES_USER']
PG_PASSWORD = os.environ['POSTGRES_PASSWORD']
PG_PORT = os.environ['POSTGRES_PORT']

PG_URL = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'
