FROM python:3.14

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app/

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./scripts/prestart.sh /app/prestart.sh

COPY ./alembic.ini ./alembic.ini

RUN chmod +x /app/prestart.sh

EXPOSE 5000 

CMD ./prestart.sh