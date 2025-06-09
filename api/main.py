from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.models import get_db, Movie
from ml.nmf_recommender import NMFRecommender

app = FastAPI(title="Movie Recommendation System", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize recommender
recommender = NMFRecommender()
try:
    # Look for model in ml folder
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(project_root, "ml", "nmf_model.pkl")
    recommender.load_model(model_path)
    print("Model loaded successfully")
except FileNotFoundError:
    print("Model not found. Please run train_model.py first.")
    recommender = None

@app.get("/")
async def read_root():
    """Serve the main HTML page"""
    return FileResponse('static/index.html')

@app.get("/movies")
async def get_movies(db: Session = Depends(get_db)):
    """Get all movies"""
    movies = db.query(Movie).all()
    return [
        {
            "movie_id": movie.movie_id,
            "title": movie.title,
            "genre": movie.genre,
            "description": movie.description,
            "year": movie.year,
            "director": movie.director
        }
        for movie in movies
    ]

@app.get("/recommendations/{movie_id}")
async def get_recommendations(movie_id: int, db: Session = Depends(get_db)):
    """Get movie recommendations for a given movie ID"""
    if recommender is None:
        raise HTTPException(status_code=500, detail="Recommendation model not available")
    
    # Check if movie exists
    movie = db.query(Movie).filter(Movie.movie_id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    try:
        # Get recommendations
        recommended_ids = recommender.get_movie_recommendations(movie_id, 5)
        
        # Get movie details for recommendations
        recommended_movies = []
        for rec_id in recommended_ids:
            rec_movie = db.query(Movie).filter(Movie.movie_id == rec_id).first()
            if rec_movie:
                recommended_movies.append({
                    "movie_id": rec_movie.movie_id,
                    "title": rec_movie.title,
                    "genre": rec_movie.genre,
                    "description": rec_movie.description,
                    "year": rec_movie.year,
                    "director": rec_movie.director
                })
        
        return {
            "movie_id": movie_id,
            "movie_title": movie.title,
            "recommendations": recommended_movies
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)