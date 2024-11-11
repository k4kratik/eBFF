FROM python:3.9.18-alpine3.19
# FROM python:3.9-slim-bullseye

COPY bot.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

# ENTRYPOINT [ "python", "bot.py" ]

CMD ["python", "-m", "uvicorn", "main:api", "--reload", "--host", "0.0.0.0", "--port", "3000", "--log-level", "info"]
