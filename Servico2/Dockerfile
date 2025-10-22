FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

ENV PYTHONPATH=/app
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

CMD ["python", "run.py"]