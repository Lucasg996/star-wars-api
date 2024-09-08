document.addEventListener('DOMContentLoaded', () => {
    const additionalDetailsContainer = document.getElementById('additional-details');
    const loadingIndicator = document.getElementById('loading');

    function createListItems(items) {
        return items.map(item => `<li>${item.name}</li>`).join('');
    }

    const movieId = window.location.pathname.split('/')[2];
    fetch(`/movie/${movieId}/details`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        }
        .then(data => {
            loadingIndicator.style.display = 'none';
            additionalDetailsContainer.style.display = 'block';

            document.getElementById('characters-list').innerHTML = createListItems(data.characters);
            document.getElementById('planets-list').innerHTML = createListItems(data.planets);
            document.getElementById('starships-list').innerHTML = createListItems(data.starships);
            document.getElementById('vehicles-list').innerHTML = createListItems(data.vehicles);
            document.getElementById('species-list').innerHTML = createListItems(data.species);
        })
        .catch(error => {
            console.error('Error fetching additional details:', error);
            loadingIndicator.textContent = 'Failed to load details.';
        });
});

