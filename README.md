# 🐧 Penguins ML Deployment

An end-to-end **Machine Learning deployment project** that uses the **Palmer Penguins Dataset** to predict the penguin species. The trained ML model is deployed as a **FastAPI** and containerized using **Docker**.

## 📌 Project Overview

This project demonstrates how to take a trained Machine Learning model and make it available as an API using FastAPI, then package the complete application inside a Docker container.

### Workflow

```text
Palmer Penguins Dataset
        ↓
Data Preprocessing
        ↓
Model Training
        ↓
Save Model (.pkl)
        ↓
FastAPI Application
        ↓
Docker Image
        ↓
Docker Container
        ↓
REST API
```

## 🛠️ Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Joblib
* FastAPI
* Uvicorn
* Docker

## 📂 Project Structure

```text
penguins-ml-deployment/
│
├── maincode.py
├── penguins_model.pkl
├── requirements.txt
├── Dockerfile
└── README.md
```

### File Description

| File                 | Description                                       |
| -------------------- | ------------------------------------------------- |
| `maincode.py`        | FastAPI application containing the prediction API |
| `penguins_model.pkl` | Trained Machine Learning model                    |
| `requirements.txt`   | Required Python dependencies                      |
| `Dockerfile`         | Instructions for building the Docker image        |
| `README.md`          | Project documentation                             |

## 🤖 Machine Learning Model

**Dataset:** Palmer Penguins Dataset

The model predicts the **penguin species** based on input features such as:

* Bill length
* Bill depth
* Flipper length
* Body mass
* Island
* Sex

### Prediction

The API returns the predicted penguin species based on the input features.

## 🚀 Run the Project Locally

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd penguins-ml-deployment
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI

```bash
uvicorn maincode:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### 4. Open API Documentation

FastAPI automatically provides interactive API documentation.

```text
http://127.0.0.1:8000/docs
```

## 🐳 Run Using Docker

### 1. Build Docker Image

```bash
docker build -t penguins-api .
```

### 2. Run Docker Container

```bash
docker run -p 8000:8000 penguins-api
```

The application will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

## 🔄 Docker Deployment Flow

```text
Dockerfile
    ↓
docker build
    ↓
Docker Image
    ↓
docker run
    ↓
Docker Container
    ↓
FastAPI + ML Model
    ↓
Prediction API
```

## 📡 API

The FastAPI application accepts penguin feature values and uses the trained model to generate a prediction.

Example endpoint:

```text
POST /predict
```

The API receives the required penguin features and returns the predicted species.

## 🎯 Project Objective

The main objective of this project is to understand the complete process of deploying a Machine Learning model:

```text
Train Model
     ↓
Save Model
     ↓
Create API
     ↓
Test API
     ↓
Create Dockerfile
     ↓
Build Docker Image
     ↓
Run Docker Container
     ↓
Expose ML Model as API
```

## 👨‍💻 Author

**Ranjith**

Data Science | Machine Learning | Python | FastAPI | Docker
