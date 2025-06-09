class MovieRecommendationApp {
    constructor() {
        this.movies = [];
        this.selectedMovie = null;
        this.init();
    }

    async init() {
        await this.loadMovies();
        this.setupEventListeners();
    }

    async loadMovies() {
        try {
            const response = await fetch('/movies');
            if (!response.ok) {
                throw new Error('Failed to load movies');
            }
            this.movies = await response.json();
            this.renderMovies(this.movies);
        } catch (error) {
            console.error('Error loading movies:', error);
            this.showError('Failed to load movies. Please try again.');
        }
    }

    renderMovies(movies) {
        const moviesGrid = document.getElementById('moviesGrid');
        moviesGrid.innerHTML = '';

        movies.forEach(movie => {
            const movieCard = this.createMovieCard(movie);
            moviesGrid.appendChild(movieCard);
        });
    }

    createMovieCard(movie) {
        const card = document.createElement('div');
        card.className = 'movie-card';
        card.dataset.movieId = movie.movie_id;
        
        card.innerHTML = `
            <div class="movie-title">${movie.title}</div>
            <div class="movie-meta">
                <span class="movie-genre">${movie.genre}</span>
                <span class="movie-year">${movie.year}</span>
            </div>
            <div class="movie-description">${movie.description}</div>
            <div style="margin-top: 10px; font-size: 0.9rem; color: #718096;">
                <strong>Director:</strong> ${movie.director}
            </div>
        `;

        card.addEventListener('click', () => this.selectMovie(movie));
        return card;
    }

    async selectMovie(movie) {
        // Update UI to show selected movie
        document.querySelectorAll('.movie-card').forEach(card => {
            card.classList.remove('selected');
        });
        
        const selectedCard = document.querySelector(`[data-movie-id="${movie.movie_id}"]`);
        if (selectedCard) {
            selectedCard.classList.add('selected');
        }

        this.selectedMovie = movie;
        this.showLoadingSpinner();

        try {
            await this.loadRecommendations(movie.movie_id);
        } catch (error) {
            console.error('Error loading recommendations:', error);
            this.showError('Failed to load recommendations. Please try again.');
        } finally {
            this.hideLoadingSpinner();
        }
    }

    async loadRecommendations(movieId) {
        const response = await fetch(`/recommendations/${movieId}`);
        if (!response.ok) {
            throw new Error('Failed to load recommendations');
        }
        
        const data = await response.json();
        this.renderRecommendations(data);
    }

    renderRecommendations(data) {
        const recommendationsSection = document.getElementById('recommendationsSection');
        const selectedMovieDiv = document.getElementById('selectedMovie');
        const recommendationsGrid = document.getElementById('recommendationsGrid');

        // Show selected movie info
        selectedMovieDiv.innerHTML = `
            <h3>Because you're interested in: "${data.movie_title}"</h3>
            <p>Here are some movies you might also enjoy:</p>
        `;

        // Render recommendations
        recommendationsGrid.innerHTML = '';
        
        if (data.recommendations.length === 0) {
            recommendationsGrid.innerHTML = '<p>No recommendations available for this movie.</p>';
        } else {
            data.recommendations.forEach(movie => {
                const recCard = this.createRecommendationCard(movie);
                recommendationsGrid.appendChild(recCard);
            });
        }

        // Show recommendations section
        recommendationsSection.style.display = 'block';
        recommendationsSection.scrollIntoView({ behavior: 'smooth' });
    }

    createRecommendationCard(movie) {
        const card = document.createElement('div');
        card.className = 'recommendation-card';
        
        card.innerHTML = `
            <div class="movie-title">${movie.title}</div>
            <div class="movie-meta">
                <span class="movie-genre">${movie.genre}</span>
                <span class="movie-year">${movie.year}</span>
            </div>
            <div class="movie-description">${movie.description}</div>
            <div style="margin-top: 10px; font-size: 0.9rem; color: #718096;">
                <strong>Director:</strong> ${movie.director}
            </div>
        `;

        card.addEventListener('click', () => {
            // Find the movie in our movies array and select it
            const fullMovie = this.movies.find(m => m.movie_id === movie.movie_id);
            if (fullMovie) {
                this.selectMovie(fullMovie);
                // Scroll back to movies section
                document.querySelector('.movies-section').scrollIntoView({ behavior: 'smooth' });
            }
        });

        return card;
    }

    setupEventListeners() {
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', (e) => {
            this.filterMovies(e.target.value);
        });
    }

    filterMovies(searchTerm) {
        const filteredMovies = this.movies.filter(movie => 
            movie.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
            movie.genre.toLowerCase().includes(searchTerm.toLowerCase()) ||
            movie.director.toLowerCase().includes(searchTerm.toLowerCase())
        );
        this.renderMovies(filteredMovies);
    }

    showLoadingSpinner() {
        document.getElementById('loadingSpinner').style.display = 'flex';
    }

    hideLoadingSpinner() {
        document.getElementById('loadingSpinner').style.display = 'none';
    }

    showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        
        const container = document.querySelector('.container');
        container.insertBefore(errorDiv, container.firstChild);
        
        // Remove error message after 5 seconds
        setTimeout(() => {
            errorDiv.remove();
        }, 5000);
    }
}

// Initialize the app when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new MovieRecommendationApp();
});