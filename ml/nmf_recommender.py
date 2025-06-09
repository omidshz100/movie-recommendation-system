import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
from sqlalchemy import create_engine

class NMFRecommender:
    def __init__(self, n_components=10):
        self.n_components = n_components
        self.model = None
        self.user_features = None
        self.item_features = None
        self.user_movie_matrix = None
        self.movie_ids = None
        
    def load_data(self):
        """Load rating data from database"""
        engine = create_engine("sqlite:///movies.db")
        
        # Load ratings
        ratings_df = pd.read_sql_query(
            "SELECT user_id, movie_id, rating FROM ratings", 
            engine
        )
        
        # Create user-movie matrix
        self.user_movie_matrix = ratings_df.pivot_table(
            index='user_id', 
            columns='movie_id', 
            values='rating', 
            fill_value=0
        )
        
        self.movie_ids = self.user_movie_matrix.columns.tolist()
        return self.user_movie_matrix
    
    def train(self):
        """Train the NMF model"""
        if self.user_movie_matrix is None:
            self.load_data()
            
        # Initialize and fit NMF model
        self.model = NMF(n_components=self.n_components, random_state=42, max_iter=200)
        self.user_features = self.model.fit_transform(self.user_movie_matrix)
        self.item_features = self.model.components_
        
        print(f"NMF model trained with {self.n_components} components")
        
    def get_movie_recommendations(self, movie_id, n_recommendations=5):
        """Get recommendations for a specific movie based on item similarity"""
        if self.model is None:
            raise ValueError("Model not trained. Call train() first.")
            
        if movie_id not in self.movie_ids:
            return []
            
        # Get the index of the movie in our matrix
        movie_idx = self.movie_ids.index(movie_id)
        
        # Get the feature vector for this movie
        movie_features = self.item_features[:, movie_idx].reshape(1, -1)
        
        # Calculate similarity with all other movies
        similarities = cosine_similarity(movie_features, self.item_features.T)[0]
        
        # Get indices of most similar movies (excluding the movie itself)
        similar_indices = np.argsort(similarities)[::-1][1:n_recommendations+1]
        
        # Convert indices back to movie IDs
        recommended_movie_ids = [self.movie_ids[idx] for idx in similar_indices]
        
        return recommended_movie_ids
    
    def save_model(self, filepath='nmf_model.pkl'):
        """Save the trained model"""
        model_data = {
            'model': self.model,
            'user_features': self.user_features,
            'item_features': self.item_features,
            'movie_ids': self.movie_ids,
            'user_movie_matrix': self.user_movie_matrix
        }
        
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath='nmf_model.pkl'):
        """Load a pre-trained model"""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Model file {filepath} not found")
            
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
            
        self.model = model_data['model']
        self.user_features = model_data['user_features']
        self.item_features = model_data['item_features']
        self.movie_ids = model_data['movie_ids']
        self.user_movie_matrix = model_data['user_movie_matrix']
        
        print(f"Model loaded from {filepath}")