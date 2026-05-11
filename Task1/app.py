from fastapi import FastAPI
import pandas as pd
import numpy as np

# Load datasets
books = pd.read_csv("books.csv")
ratings = pd.read_csv("ratings.csv")

# Create FastAPI app
app = FastAPI()

# Home route
@app.get("/")
def home():

    return {
        "message": "Book Recommendation API is Running"
    }

def recommend_for_new_user(top_n=10):

    return books.sort_values(
        by='average_rating',
        ascending=False
    ).head(top_n)[[
        'book_id',
        'title',
        'average_rating'
    ]]


# Recommendation function
def recommend(user_id, top_n=10):

    # Cold-start handling
    if user_id not in ratings['user_id'].unique():

        recommendations = books.sort_values(
            by='average_rating',
            ascending=False
        ).head(top_n)

    else:

        recommendations = books.sort_values(
            by='average_rating',
            ascending=False
        ).head(top_n)

    return recommendations[
        ['book_id', 'title', 'average_rating']
    ]

# API endpoint
@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int):

    recs = recommend(user_id)

    return recs.to_dict(orient='records')