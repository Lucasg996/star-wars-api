const movies = [
    { title: "A New Hope", image: "/static/images/new_hope.jpg", apiId: 1 },
    { title: "The Empire Strikes Back", image: "/static/images/empire_strikes_back.jpg", apiId: 2 },
    { title: "Return of the Jedi", image: "/static/images/return_of_the_jedi.jpg", apiId: 3 },
    { title: "The Phantom Menace", image: "/static/images/phantom_menace.jpg", apiId: 4 },
    { title: "Attack of the Clones", image: "/static/images/attack_of_the_clones.jpg", apiId: 5 },
    { title: "Revenge of the Sith", image: "/static/images/revenge_of_the_sith.jpg", apiId: 6 }
];

export function displayMovies() {
    const moviesContainer = document.getElementById('movies');
    movies.forEach(movie => {
        const movieElement = document.createElement('div');
        movieElement.className = 'movie';
        movieElement.innerHTML = `
            <img src="${movie.image}" alt="${movie.title}">
            <div class="movie-title">${movie.title}</div>
        `;
        movieElement.addEventListener('click', () => window.location.href = `/movie/${movie.apiId}`);
        moviesContainer.appendChild(movieElement);
    });
}

document.addEventListener('DOMContentLoaded', displayMovies);




