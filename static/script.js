document.getElementById('recommendButton').addEventListener('click', function() {
    const movieTitle = document.getElementById('movieTitle').value;
    fetch(`/recommend?title=${encodeURIComponent(movieTitle)}`)
        .then(response => response.json())
        .then(data => {
            const recommendationsDiv = document.getElementById('recommendations');
            recommendationsDiv.innerHTML = ''; 

            if (data.length > 0) {
                data.forEach(movie => {
                    const movieDiv = document.createElement('div');
                    movieDiv.classList.add('recommendation');

                    const movieImg = document.createElement('img');
                    movieImg.src = movie.poster_path;
                    movieImg.alt = movie.title;

                    const movieTitle = document.createElement('p');
                    movieTitle.textContent = movie.title;

                    movieDiv.appendChild(movieImg);
                    movieDiv.appendChild(movieTitle);
                    recommendationsDiv.appendChild(movieDiv);
                });
            } else {
                const errorMessage = document.createElement('p');
                errorMessage.textContent = 'No se encontraron recomendaciones.';
                errorMessage.classList.add('error-message');
                recommendationsDiv.appendChild(errorMessage);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

