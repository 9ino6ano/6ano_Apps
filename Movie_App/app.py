from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
from datetime import datetime

app = Flask(__name__)

API_KEY = 'YOUR_TMDB_API_KEY'  # Replace with your TMDb API key

# SQLite database initialization
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT,
        release_date TEXT
    )
''')
conn.commit()
conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch_movies', methods=['POST'])
def fetch_movies():
    genre = request.form.get('genre')
    current_year = datetime.now().year
    upcoming_year = current_year + 1

    # Fetch movies from TMDb API
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&primary_release_year={current_year}&with_genres={genre}'
    response = requests.get(url)
    movies = response.json().get('results', [])

    # Save movies to the local database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM movies WHERE genre = ?', (genre,))
    for movie in movies:
        cursor.execute('INSERT INTO movies (title, genre, release_date) VALUES (?, ?, ?)',
                       (movie['title'], genre, movie['release_date']))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Movies fetched and saved successfully!'})


@app.route('/search_movies', methods=['POST'])
def search_movies():
    query = request.form.get('query')

    # Search movies in the local database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies WHERE title LIKE ?', (f'%{query}%',))
    movies = cursor.fetchall()
    conn.close()

    return jsonify({'movies': movies})


if __name__ == '__main__':
    app.run(debug=True)


