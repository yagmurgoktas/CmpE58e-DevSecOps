FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt /app/
COPY src/main.py /app/
COPY src/app/ /app/app/

RUN apt-get update && apt-get upgrade -y && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
