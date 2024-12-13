FROM python:3.12-slim
ENV PYTHONUNBUFFERED 1

USER root

RUN python -m ensurepip --upgrade \
    && python -m pip install --upgrade pip setuptools wheel

WORKDIR /app

RUN python -m venv .env \
    && . .env/bin/activate

COPY requirements.txt .
COPY create_img.py .
COPY main.py .
COPY thingspeak_api.py .

RUN  pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/main.py"]