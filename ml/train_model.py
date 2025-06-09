from nmf_recommender import NMFRecommender

def train_and_save_model():
    """Train the NMF model and save it"""
    print("Training NMF recommendation model...")
    
    # Initialize recommender
    recommender = NMFRecommender(n_components=10)
    
    # Load data and train
    recommender.load_data()
    recommender.train()
    
    # Save the model
    recommender.save_model('nmf_model.pkl')
    
    # Test the model
    print("\nTesting model with movie ID 1:")
    recommendations = recommender.get_movie_recommendations(1, 5)
    print(f"Recommended movies: {recommendations}")
    
    print("Model training completed!")

if __name__ == "__main__":
    train_and_save_model()