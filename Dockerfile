FROM python:3.8.5-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000 5001

CMD ["python", "run_config.py"]

COPY . .

