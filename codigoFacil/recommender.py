import requests


API_KEY = 'b96ce5641860dc081f62086adc29f811'  
BASE_URL = 'https://api.themoviedb.org/3'

def get_movie_data(movie_title):
    search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_title}"
    response = requests.get(search_url)
    data = response.json()
    
    if data['results']:
        return data['results'][0] 
    else:
        return None


def get_recommendations(movie_id):
    recommendation_url = f"{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}"
    response = requests.get(recommendation_url)
    data = response.json()
    return data['results']


def main():
    movie_title = input("Ingresa el título de una película: ")
    movie_data = get_movie_data(movie_title)
    
    if movie_data:
        movie_id = movie_data['id']
        recommendations = get_recommendations(movie_id)
        
        if recommendations:
            print(f"\nRecomendaciones basadas en '{movie_data['title']}':\n")
            for movie in recommendations:
                print(f" - {movie['title']} (ID: {movie['id']})")
        else:
            print("No se encontraron recomendaciones.")
    else:
        print("No se encontró la película. Asegúrate de que el título sea correcto.")

if __name__ == "__main__":
    main()
