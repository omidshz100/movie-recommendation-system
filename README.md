# Movie Recommendation System
A web-based movie recommendation system built with FastAPI and machine learning using Non-negative Matrix Factorization (NMF) algorithm.
## 🎬 Overview
This project implements a content-based movie recommendation system that suggests similar movies based on user ratings. The system uses Non-negative Matrix Factorization (NMF) to analyze user-movie rating patterns and generate personalized recommendations.
## 🏗️ Project Structure

## 🧠 NMF Algorithm Explanation

### What is Non-negative Matrix Factorization (NMF)?

Non-negative Matrix Factorization is a dimensionality reduction technique that decomposes a matrix into two lower-dimensional matrices with non-negative elements. In the context of recommendation systems, NMF helps identify latent features that explain user preferences and item characteristics.

### How NMF Works in This Project

#### 1. **User-Movie Rating Matrix**
The system starts with a user-movie rating matrix `R` where:
- Rows represent users
- Columns represent movies
- Values represent ratings (1-5 scale)
- Missing values are filled with 0

#### 2. **Matrix Factorization**
NMF decomposes the rating matrix `R` into two matrices:
- **User Features Matrix (W)**: `n_users × n_components`
- **Item Features Matrix (H)**: `n_components × n_movies`

Where:
- `n_components` is the number of latent features (default: 10)
- All values in W and H are non-negative

#### 3. **Latent Features**
The `n_components` represent hidden patterns such as:
- Genre preferences (action, comedy, drama)
- Movie characteristics (budget, cast popularity)
- User demographics or viewing habits

#### 4. **Recommendation Generation**
For movie recommendations, the system:
1. Extracts the target movie's feature vector from matrix H
2. Calculates cosine similarity with all other movies
3. Returns the most similar movies as recommendations

```python
# Cosine similarity calculation
similarity = cosine_similarity(target_movie_features, all_movie_features)
### Implementation Details
The NMF implementation in this project:

- Components : 10 latent features (configurable)
- Algorithm : Coordinate Descent (scikit-learn default)
- Initialization : Random (with fixed seed for reproducibility)
- Max Iterations : 200
- Similarity Metric : Cosine similarity for item-to-item recommendations
### Advantages of NMF for Recommendations
1. Interpretability : Non-negative constraints make features more interpretable
2. Sparsity Handling : Works well with sparse rating matrices
3. Scalability : Efficient computation for large datasets
4. Cold Start : Can handle new items through feature similarity
## 🚀 Features
- Web Interface : Clean, responsive UI for browsing movies and getting recommendations
- RESTful API : FastAPI backend with automatic documentation
- Real-time Recommendations : Get similar movies instantly
- Movie Database : SQLite database with movies and ratings
- Machine Learning : NMF-based recommendation engine
- Static File Serving : Integrated frontend hosting
## 📋 Requirements
- Python 3.8+
- FastAPI
- scikit-learn
- pandas
- numpy
- SQLAlchemy
- uvicorn
## 🛠️ Installation
1. Clone the repository :
```
git clone <repository-url>
cd RecommSystemForMovies
```
2. Create and activate virtual environment :
```
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. Install dependencies :
```
pip install -r requirements.txt
```
4. Set up the database :
```
python database/setup_db.py
```
5. Train the recommendation model :
```
python ml/train_model.py
```
## 🏃‍♂️ Running the Application
1. Start the FastAPI server :
```
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
2. Access the application :
- Web Interface : http://localhost:8000
- API Documentation : http://localhost:8000/docs
- Alternative API Docs : http://localhost:8000/redoc
## 🔌 API Endpoints
### Movies
- GET / - Web interface
- GET /movies - Get all movies
- GET /movies/{movie_id} - Get specific movie details
### Recommendations
- GET /recommendations/{movie_id} - Get movie recommendations
  - Parameters :
    - movie_id : ID of the movie to get recommendations for
    - limit : Number of recommendations (default: 5)
### Example API Usage
```
# Get all movies
curl http://localhost:8000/movies

# Get recommendations for movie ID 1
curl http://localhost:8000/recommendations/1?limit=5
```
## 🗄️ Database Schema
### Movies Table
```
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    year INTEGER,
    rating FLOAT
);
```
### Ratings Table
```
CREATE TABLE ratings (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    rating FLOAT NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movies (id)
);
```
## 🧪 Model Training
The NMF model can be retrained with new data:

```
python ml/train_model.py
```
This will:

1. Load rating data from the database
2. Create user-movie matrix
3. Train NMF model with 10 components
4. Save the trained model to ml/nmf_model.pkl
5. Test the model with sample recommendations
## 🎯 Model Performance
The NMF model performance depends on:

- Data Quality : More ratings improve recommendations
- Number of Components : Balance between complexity and interpretability
- Rating Sparsity : Dense matrices generally perform better
### Tuning Parameters
You can adjust the model by modifying ml/nmf_recommender.py :

```
# Increase components for more detailed features
recommender = NMFRecommender(n_components=20)

# Adjust max iterations for convergence
self.model = NMF(n_components=self.n_components, max_iter=500)
```
## 🔧 Configuration
### Environment Variables
Create a .env file for configuration:

```
DATABASE_URL=sqlite:///api/movies.db
MODEL_PATH=ml/nmf_model.pkl
API_HOST=0.0.0.0
API_PORT=8000
```
### Model Parameters
Adjust in ml/nmf_recommender.py :

- n_components : Number of latent features (default: 10)
- max_iter : Maximum training iterations (default: 200)
- random_state : Seed for reproducibility (default: 42)
## 🚀 Deployment
### Docker Deployment
Create a Dockerfile :

```
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
### Production Considerations
- Use PostgreSQL instead of SQLite for production
- Implement user authentication
- Add rate limiting
- Use Redis for caching recommendations
- Monitor model performance and retrain periodically
## 🤝 Contributing
1. Fork the repository
2. Create a feature branch ( git checkout -b feature/amazing-feature )
3. Commit your changes ( git commit -m 'Add amazing feature' )
4. Push to the branch ( git push origin feature/amazing-feature )
5. Open a Pull Request
## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- scikit-learn for the NMF implementation
- FastAPI for the excellent web framework
- SQLAlchemy for database ORM
- MovieLens dataset inspiration for the rating system
## 📞 Support
If you encounter any issues or have questions:

1. Check the API documentation at /docs
2. Review the console output for error messages
3. Ensure the model is trained before making recommendations
4. Verify database setup is complete
Happy Movie Recommending! 🎬🍿

```

## Quick Steps:

1. **Select ALL the text** above between the ``` markers (starting from `# Movie 
Recommendation System` to `**Happy Movie Recommending! 🎬🍿**`)
2. **Copy it** (Cmd+C on Mac)
3. **Open your README.md file** in Trae AI
4. **Select all existing content** (Cmd+A)
5. **Paste the new content** (Cmd+V)
6. **Save the file** (Cmd+S)

That's it! Your README.md will be completely updated with comprehensive documentation.
```