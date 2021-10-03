FROM python:3.8-slim

COPY ./ /app
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "library_api.app:app", "--host=127.0.0.1", "--reload"]