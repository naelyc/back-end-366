FROM bitnami/python:3.11.1
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 8000
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
