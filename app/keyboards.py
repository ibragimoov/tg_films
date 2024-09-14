from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_items_by_category

import requests

def films():
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ru-RU&sort_by=popularity.desc"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyODkwODE1YmZiOWM1ZTNjZjJmZDkwNDUyMGE0NmJlYyIsIm5iZiI6MTcyNjMwMTI3NS44NDI1Mywic3ViIjoiNjZlNTQzY2ZmYjM5MTRlMjU1ZmQ1ODNkIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.2T_mWV3Gr5IMlLxWbe0m0VpqNhhn6N3KqmFdBmfPAzM"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    films = data["results"]

    keyboard = InlineKeyboardBuilder()

    for film in films:
        keyboard.add(InlineKeyboardButton(text=film["title"], callback_data=str(film["id"])))

    return keyboard.adjust(2).as_markup()
