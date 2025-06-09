import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Rating

# Sample movie data
MOVIES_DATA = [
    {"movie_id": 1, "title": "The Matrix", "genre": "Sci-Fi", "description": "A computer hacker learns about the true nature of reality.", "year": 1999, "director": "The Wachowskis"},
    {"movie_id": 2, "title": "Inception", "genre": "Sci-Fi", "description": "A thief who steals corporate secrets through dream-sharing technology.", "year": 2010, "director": "Christopher Nolan"},
    {"movie_id": 3, "title": "The Godfather", "genre": "Crime", "description": "The aging patriarch of an organized crime dynasty transfers control to his reluctant son.", "year": 1972, "director": "Francis Ford Coppola"},
    {"movie_id": 4, "title": "Pulp Fiction", "genre": "Crime", "description": "The lives of two mob hitmen, a boxer, and others intertwine in four tales of violence.", "year": 1994, "director": "Quentin Tarantino"},
    {"movie_id": 5, "title": "The Dark Knight", "genre": "Action", "description": "Batman faces the Joker, a criminal mastermind who wants to plunge Gotham into anarchy.", "year": 2008, "director": "Christopher Nolan"},
    {"movie_id": 6, "title": "Forrest Gump", "genre": "Drama", "description": "The presidencies of Kennedy and Johnson through the eyes of an Alabama man.", "year": 1994, "director": "Robert Zemeckis"},
    {"movie_id": 7, "title": "Interstellar", "genre": "Sci-Fi", "description": "A team of explorers travel through a wormhole in space to save humanity.", "year": 2014, "director": "Christopher Nolan"},
    {"movie_id": 8, "title": "The Shawshank Redemption", "genre": "Drama", "description": "Two imprisoned men bond over years, finding solace and redemption.", "year": 1994, "director": "Frank Darabont"},
    {"movie_id": 9, "title": "Goodfellas", "genre": "Crime", "description": "The story of Henry Hill and his life in the mob.", "year": 1990, "director": "Martin Scorsese"},
    {"movie_id": 10, "title": "Fight Club", "genre": "Drama", "description": "An insomniac office worker forms an underground fight club.", "year": 1999, "director": "David Fincher"},
    {"movie_id": 11, "title": "Avatar", "genre": "Sci-Fi", "description": "A paraplegic Marine dispatched to the moon Pandora on a unique mission.", "year": 2009, "director": "James Cameron"},
    {"movie_id": 12, "title": "Titanic", "genre": "Romance", "description": "A seventeen-year-old aristocrat falls in love with a poor artist aboard the Titanic.", "year": 1997, "director": "James Cameron"},
    {"movie_id": 13, "title": "The Lord of the Rings", "genre": "Fantasy", "description": "A meek Hobbit and companions set out on a journey to destroy the One Ring.", "year": 2001, "director": "Peter Jackson"},
    {"movie_id": 14, "title": "Star Wars", "genre": "Sci-Fi", "description": "Luke Skywalker joins forces with a Jedi Knight to rescue a princess.", "year": 1977, "director": "George Lucas"},
    {"movie_id": 15, "title": "Jurassic Park", "genre": "Adventure", "description": "A pragmatic paleontologist visiting an almost complete theme park is tasked with protecting visitors.", "year": 1993, "director": "Steven Spielberg"},
    {"movie_id": 16, "title": "The Avengers", "genre": "Action", "description": "Earth's mightiest heroes must come together to stop an alien invasion.", "year": 2012, "director": "Joss Whedon"},
    {"movie_id": 17, "title": "Casablanca", "genre": "Romance", "description": "A cynical American expatriate struggles to decide whether to help his former lover.", "year": 1942, "director": "Michael Curtiz"},
    {"movie_id": 18, "title": "The Silence of the Lambs", "genre": "Thriller", "description": "A young FBI cadet must receive help from Hannibal Lecter to catch another serial killer.", "year": 1991, "director": "Jonathan Demme"},
    {"movie_id": 19, "title": "Saving Private Ryan", "genre": "War", "description": "Following D-Day, a group of soldiers go behind enemy lines to retrieve a paratrooper.", "year": 1998, "director": "Steven Spielberg"},
    {"movie_id": 20, "title": "Schindler's List", "genre": "Drama", "description": "In German-occupied Poland, Oskar Schindler gradually becomes concerned for his Jewish workforce.", "year": 1993, "director": "Steven Spielberg"}
]

def create_database():
    engine = create_engine("sqlite:///movies.db")
    Base.metadata.create_all(bind=engine)
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    # Add movies
    for movie_data in MOVIES_DATA:
        movie = Movie(**movie_data)
        db.add(movie)
    
    # Generate random ratings (user_id 1-50, ratings 1-5)
    for user_id in range(1, 51):
        # Each user rates 10-15 random movies
        num_ratings = random.randint(10, 15)
        rated_movies = random.sample(range(1, 21), num_ratings)
        
        for movie_id in rated_movies:
            rating = round(random.uniform(1, 5), 1)
            rating_obj = Rating(user_id=user_id, movie_id=movie_id, rating=rating)
            db.add(rating_obj)
    
    db.commit()
    db.close()
    print("Database created successfully with sample data!")

if __name__ == "__main__":
    create_database()