FROM python:3.9.18-alpine3.19

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "-m", "uvicorn", "main:api", "--host", "0.0.0.0", "--port", "3000", "--log-level", "info"]
