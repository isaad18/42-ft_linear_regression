FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"

RUN pip install --no-cache-dir flake8

COPY . .

CMD ["python", "-m", "python"]
