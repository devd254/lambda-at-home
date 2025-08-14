FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install cloudpickle

COPY handlers/ ./handlers
COPY src/ ./src

CMD ["python", "-u", "-c", "import time; time.sleep(3600)"]