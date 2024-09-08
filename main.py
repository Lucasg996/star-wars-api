from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx, asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Actualiza el mapeo basado en la información real de la API
episode_to_id = {
    1: 4,  # Episodio 1 - The Phantom Menace
    2: 5,  # Episodio 2 - Attack of the Clones
    3: 6,  # Episodio 3 - Revenge of the Sith
    4: 1,  # Episodio 4 - A New Hope
    5: 2,  # Episodio 5 - The Empire Strikes Back
    6: 3,  # Episodio 6 - Return of the Jedi
}

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://swapi.dev/api/films/')
        data = response.json()

    movies = []
    for movie in data['results']:
        episode_id = movie["episode_id"]
        movies.append({
            "id": episode_to_id[episode_id],
            "title": movie["title"],
            "image": f"/static/images/{episode_id}.jpg",
        })

    return templates.TemplateResponse("index.html", {"request": request, "movies": movies})

@app.get("/movie/{movie_id}", response_class=HTMLResponse)
async def movie_detail(request: Request, movie_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://swapi.dev/api/films/{movie_id}/')
        movie = response.json()

        characters = await asyncio.gather(*(client.get(url) for url in movie["characters"]))
        characters = [char.json() for char in characters]

        planets = await asyncio.gather(*(client.get(url) for url in movie["planets"]))
        planets = [planet.json() for planet in planets]

        starships = await asyncio.gather(*(client.get(url) for url in movie["starships"]))
        starships = [starship.json() for starship in starships]

        vehicles = await asyncio.gather(*(client.get(url) for url in movie["vehicles"]))
        vehicles = [vehicle.json() for vehicle in vehicles]

        species = await asyncio.gather(*(client.get(url) for url in movie["species"]))
        species = [specie.json() for specie in species]

    return templates.TemplateResponse("movie_detail.html", {
        "request": request,
        "movie": movie,
        "characters": characters,
        "planets": planets,
        "starships": starships,
        "vehicles": vehicles,
        "species": species
    })
