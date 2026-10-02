FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY maincode.py .
COPY penguins_model.pkl .
EXPOSE 8000

CMD ["uvicorn", "maincode:app", "--host", "0.0.0.0", "--port", "8000"] docker network 