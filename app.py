from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'b96ce5641860dc081f62086adc29f811'  
BASE_URL = 'https://api.themoviedb.org/3'
BASE_IMAGE_URL = 'https://image.tmdb.org/t/p/w500'

def get_movie_data(title):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(url)
    data = response.json()
    return data

def get_recommendations(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    data = response.json()
    
    recommendations = []
    if 'results' in data and len(data['results']) > 0:
        for movie in data['results'][:10]:  # Limita a 10 recomendaciones
            if movie.get('poster_path'):
                movie['poster_path'] = BASE_IMAGE_URL + movie['poster_path']
                recommendations.append(movie)
    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_title = request.args.get('title')
    movie_data = get_movie_data(movie_title)
    
    if 'results' in movie_data and len(movie_data['results']) > 0:
        movie_id = movie_data['results'][0]['id']
        recommendations = get_recommendations(movie_id)
        return jsonify(recommendations)
    else:
        return jsonify([])  # Devuelve una lista vacía si no hay resultados

if __name__ == '__main__':
    app.run(debug=True)
