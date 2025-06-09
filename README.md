# 🎬 Movie Recommendation System

A web-based movie recommendation system that provides AI-powered suggestions. This application allows users to browse a movie catalog, search for titles, and receive personalized recommendations based on the Non-negative Matrix Factorization (NMF) algorithm.

The frontend is built with vanilla HTML, CSS, and JavaScript, and the backend is a RESTful API powered by Python and FastAPI.

---

## ✨ Features

- **Dynamic Movie Catalog**: Browse a grid of movies loaded directly from the database.
- **Live Search**: Instantly filter movies by title, genre, or director.
- **AI-Powered Recommendations**: Select any movie to get a list of similar titles based on collaborative filtering.
- **Clean & Responsive UI**: A modern and easy-to-use interface.
- **RESTful Backend**: A robust API serves all movie data and recommendation logic.

---

## 🧠 How It Works

The recommendation engine uses **Non-negative Matrix Factorization (NMF)**, a collaborative filtering technique.

1.  **User-Movie Matrix**: The system first builds a matrix where rows represent users and columns represent movies. The cells contain user ratings.
2.  **Factorization**: NMF breaks this large matrix down into two smaller matrices: one representing user features (e.g., preference for a genre) and another representing movie features.
3.  **Similarity Calculation**: To find movies similar to a given movie, the system calculates the cosine similarity between that movie's feature vector and all other movies' feature vectors.
4.  **Top Recommendations**: The movies with the highest similarity scores are then returned as recommendations.

---

## ⚙️ Technologies Used

| Category      | Technology                                       |
| ------------- | ------------------------------------------------ |
| **Backend** | Python, FastAPI, Uvicorn                         |
| **Database** | SQLAlchemy, SQLite                               |
| **ML/Data** | Scikit-learn, Pandas, NumPy                      |
| **Frontend** | HTML, CSS, JavaScript                            |

---

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### 1. Prerequisites

- Python 3.7+
- A tool for creating virtual environments (e.g., `venv`)

### 2. Installation

First, clone the repository and navigate into the project's root directory.

```bash
git clone [https://github.com/omidshz100/movie-recommendation-system.git](https://github.com/omidshz100/movie-recommendation-system.git)
cd movie-recommendation-system

Next, create and activate a Python virtual environment.

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

Install all the required packages from requirements.txt.

pip install -r requirements.txt

3. Project Setup
The following steps are crucial to ensure the database and machine learning model are placed where the application expects to find them. Run all commands from the root directory of the project.

Step 1: Create the Database
Run the setup script. This will create a movies.db file in the root directory.

python database/setup_db.py

Now, copy the database into the api/ folder so the application can access it.

# For macOS/Linux
cp movies.db api/

# For Windows
copy movies.db api\

Step 2: Train the ML Model
Run the training script. This script reads the movies.db file from the root and creates a model file named nmf_model.pkl.

python ml/train_model.py

Now, move the trained model into the ml/ folder so the application can use it.

# For macOS/Linux
mv nmf_model.pkl ml/

# For Windows
move nmf_model.pkl ml\

4. Run the Application
With the setup complete, change into the api directory and start the web server.

cd api
uvicorn main:app --reload

You can now access the application by navigating to https://www.google.com/search?q=http://127.0.0.1:8000 in your web browser.

📦 API Endpoints
The backend provides the following API endpoints:
Method	Path	Description
GET	/	Serves the main index.html frontend.
GET	/movies	Returns a JSON list of all movies.
GET	/recommendations/{movie_id}	Returns recommendations for a given movie_id.
GET	/static/*	Serves static files (CSS, JS).
