# 📌 Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс Movie с полями id, title, description и genre.
# 📌 Создайте список movies для хранения фильмов.
# 📌 Создайте маршрут для получения списка фильмов по жанру (метод GET).
# 📌 Реализуйте валидацию данных запроса и ответа.


from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import uvicorn
from random import randint as rnd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Genre(BaseModel):
    id: int
    name: str

class MovieIn(BaseModel):
    title: str
    description: Optional[str] = "Свободное поле"
    genre: int

class Movie(MovieIn):
    id: int
    

movies = [
    Movie(id=1,title='Movie_1', description='first movie', genre=1),
    Movie(id=2,title='Movie_2', description='second movie', genre=1),
    Movie(id=3,title='Movie_3', description='third movie', genre=4),
    Movie(id=4,title='Movie_4', description='fourth movie', genre=3)
]

genres = [
    Genre(id=1, name='comedy'),
    Genre(id=2, name='fantasy'),
    Genre(id=3, name='action'),
    Genre(id=4, name='thriller'),    
]

@app.get('/', response_model=list[Movie], summary='Получить список всех фильмов', tags=['Главная'])
async def root():
    logger.info('Вывод списка всех фильмов')
    return movies

@app.get('/{genre_name}', response_model=list[Movie], summary='Получить список фильмов по жанру', tags=['Фильмы'])
async def find_films(genre_name: str):
    genre_id = 0
    for genre in genres:
        if genre.name == genre_name:
            genre_id = genre.id
    result_list = []
    # result_list.clear()
    for movie in movies:
        if movie.genre == genre_id:
            result_list.append(movie)
    logger.info(f'Вывод списка фильмов в жанре {genre_name}')
    return result_list

@app.post("/movies/", response_model=Movie, summary='Добавить фильм', tags=['Фильмы'])
async def add_movie(movie: MovieIn):
    id = len(movies) + 1
    new_movie = Movie(
        id = id,
        title = movie.title,
        description=movie.description,
        genre=movie.genre
    )
    movies.append(new_movie)
    logger.info(f'Добавлен фильм {movie.title}')
    return new_movie


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)