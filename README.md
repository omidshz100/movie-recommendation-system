# Extera Explaination : 

That's an interesting result! The recommendations you're getting (Saving Private Ryan, Casablanca, Titanic, Pulp Fiction, Jurassic Park) are quite different from what was expected in the comment (other sci-fi movies like Inception and Interstellar).

## Analysis of the Results

The fact that The Matrix is being recommended these classic blockbuster movies instead of sci-fi films suggests a few possibilities:

### 1. **Rating Pattern Similarity**
The NMF algorithm is finding movies that have similar user rating patterns to The Matrix, rather than similar genres. This means:
- Users who rated The Matrix highly also tend to rate these other movies highly
- The recommendation is based on collaborative filtering (user behavior) rather than content-based filtering (movie attributes)

### 2. **Popular Movie Bias**
All the recommended movies are:
- Highly acclaimed blockbusters
- Movies that tend to receive high ratings from many users
- Cross-genre appeal films

This suggests the model might be biased toward recommending generally popular movies rather than genre-specific ones.

### 3. **Training Data Characteristics**
The recommendations indicate that in your training dataset:
- Users who like The Matrix also tend to like these classic films
- There might not be enough sci-fi movie data or user ratings to create strong sci-fi clusters
- The feature space learned by NMF is capturing "high-quality blockbuster" patterns rather than genre patterns

## Why This Happens

NMF works by:
1. Decomposing the user-movie rating matrix into latent factors
2. Finding movies with similar factor representations
3. The factors might represent "movie quality" or "mainstream appeal" rather than genre

## Potential Improvements

To get more genre-aware recommendations, you could:
1. **Add genre information** to the model (hybrid approach)
2. **Increase the number of components** in NMF to capture more nuanced patterns
3. **Filter recommendations by genre** after getting the similarity scores
4. **Use content-based features** alongside collaborative filtering

The current results show the model is working correctly from a collaborative filtering perspective - it's finding movies that similar users tend to enjoy together, even if they're not in the same genre.
        




# Movie Recommendation System

A lightweight, web-based movie recommendation system built with FastAPI and Scikit-learn. The application suggests movies to users based on item-to-item collaborative filtering using Non-negative Matrix Factorization (NMF).

## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [License](#license)

## About The Project

This project provides a simple yet effective movie recommendation engine accessible through a clean, responsive web interface. Users can browse a list of movies, select one they are interested in, and receive a list of five similar movies.

**Key Features:**
* **AI-Powered Recommendations**: Utilizes Scikit-learn's NMF model to generate content-aware recommendations.
* **RESTful API**: A backend built with FastAPI serves movie data and handles recommendation logic.
* **Interactive Frontend**: A vanilla JavaScript single-page application for a smooth user experience.
* **Search Functionality**: Allows users to filter the movie list by title, genre, or director.

### Built With

This project was built with the following technologies:

* **Backend**:
    * [FastAPI](https://fastapi.tiangolo.com/)
    * [Uvicorn](https://www.uvicorn.org/)
* **Machine Learning**:
    * [Scikit-learn](https://scikit-learn.org/)
    * [Pandas](https://pandas.pydata.org/)
    * [NumPy](https://numpy.org/)
* **Database**:
    * [SQLAlchemy](https://www.sqlalchemy.org/)
    * [SQLite](https://www.sqlite.org/index.html)
* **Frontend**:
    * HTML5
    * CSS3
    * JavaScript (ES6)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You must have Python 3.7 or newer installed on your system.

### Installation

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/omidshz100/movie-recommendation-system.git](https://github.com/omidshz100/movie-recommendation-system.git)
    cd movie-recommendation-system
    ```

2.  **Create and activate a virtual environment**
    ```sh
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up the database**
    This script creates `movies.db` and populates it with sample data. It will place the file in the project's root directory.
    ```sh
    python database/setup_db.py
    ```
    After creation, **move the `movies.db` file into the `api/` directory**.
    ```sh
    # On macOS/Linux
    mv movies.db api/

    # On Windows
    move movies.db api\
    ```

5.  **Train the recommendation model**
    This script trains the NMF model and saves it as `nmf_model.pkl` in the root directory.
    ```sh
    python ml/train_model.py
    ```
    After training, **move the `nmf_model.pkl` file into the `ml/` directory**.
     ```sh
    # On macOS/Linux
    mv nmf_model.pkl ml/

    # On Windows
    move nmf_model.pkl ml\
    ```

## Usage

Once the setup is complete, you can run the application.

1.  Navigate to the `api` directory:
    ```sh
    cd api
    ```

2.  Start the Uvicorn server:
    ```sh
    uvicorn main:app --reload
    ```

3.  Open your web browser and go to `http://127.0.0.1:8000`.

You can now browse the movie catalog. Click on any movie card to see a list of recommendations at the bottom of the page.

## Project Structure


movie-recommendation-system/
│
├── api/
│   ├── static/
│   │   ├── index.html
│   │   ├── style.css
│   │   └── script.js
│   ├── main.py             # FastAPI application logic
│   └── movies.db           # SQLite database file
│
├── database/
│   ├── models.py           # SQLAlchemy ORM models
│   └── setup_db.py         # Script to initialize the database
│
├── ml/
│   ├── nmf_recommender.py  # NMF model and recommendation logic
│   ├── train_model.py      # Script to train and save the model
│   └── nmf_model.pkl       # Saved scikit-learn model
│
├── .gitignore
├── README.md
└── requirements.txt


## API Reference

The following endpoints are available:

| Method | Endpoint                       | Description                                |
| ------ | ------------------------------ | ------------------------------------------ |
| `GET`  | `/`                            | Serves the HTML frontend.                  |
| `GET`  | `/movies`                      | Retrieves a list of all movies.            |
| `GET`  | `/recommendations/{movie_id}`  | Gets recommendations for a specific movie. |

## License

Distributed under the MIT License. See `LICENSE` for more information.


