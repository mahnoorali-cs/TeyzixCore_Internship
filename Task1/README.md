Book Recommendation System

Overview

This project implements a hybrid book recommendation system using collaborative filtering and content-based filtering techniques.

The system recommends personalized books to users based on:
* User ratings
* Book descriptions
* Hybrid recommendation scoring

Features

* Collaborative filtering using SVD
* Description-based filtering using TF-IDF
* Hybrid recommendation model
* Start handling for new users
* FastAPI REST API
* Evaluation metrics:
  1.Precision@K
  2.Recall@K
  3.NDCG

Technologies Used

* Python
* Pandas
* Scikit-learn
* FastAPI
* NumPy
* SciPy

Datasets

* books.csv
* ratings.csv
* to_read.csv

API Endpoint

Get Recommendations

GET /recommend/{user_id}

Run Project
Install dependencies:
pip install -r requirements.txt

Run FastAPI server:
uvicorn app:app --reload

Open Swagger UI:
http://127.0.0.####docs


Author
Mahnoor Ali
