# Test in Python console
from ml.nmf_recommender import NMFRecommender
recommender = NMFRecommender()
recommender.load_model('ml/nmf_model.pkl')

# Test sci-fi movie (The Matrix, ID=1)
recs = recommender.get_movie_recommendations(1, 5)
print(f"Recommendations for The Matrix: {recs}")

# Expected: Should include other sci-fi movies like Inception (2), Interstellar (7), etc.