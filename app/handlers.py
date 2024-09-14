from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb

import requests

router = Router()

@router.message()
async def cmd_start(message: Message):
    await message.answer('Список всех фильмов:', reply_markup=kb.films())

@router.callback_query()
async def film(callback: CallbackQuery):
    film_id = int(callback.data)

    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ru-RU&sort_by=popularity.desc"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyODkwODE1YmZiOWM1ZTNjZjJmZDkwNDUyMGE0NmJlYyIsIm5iZiI6MTcyNjMwMTI3NS44NDI1Mywic3ViIjoiNjZlNTQzY2ZmYjM5MTRlMjU1ZmQ1ODNkIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.2T_mWV3Gr5IMlLxWbe0m0VpqNhhn6N3KqmFdBmfPAzM"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    films = data["results"]

    founded_film = {}
    for film in films:
        if film["id"] == film_id:
            founded_film = film
            break

    image_link = 'https://image.tmdb.org/t/p/w500' + founded_film["poster_path"]

    text = f'<b>{founded_film["original_title"]} | {founded_film["title"]}</b>\n\n{founded_film["overview"]}'

    await callback.message.answer_photo(photo=image_link, caption=text, parse_mode='HTML')