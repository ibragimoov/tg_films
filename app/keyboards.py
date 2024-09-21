from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
import requests
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='мои книги', callback_data='my_books')],
])


def books():
    keyboard = InlineKeyboardBuilder()
    book_list = requests.get('https://www.googleapis.com/books/v1/volumes?q=search+terms')
    book_data = book_list.json()['items']

    for book in book_data:
        keyboard.add(InlineKeyboardButton(text = book['volumeInfo']['title'], callback_data='book|' + book['id']))

    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='back'))

    return keyboard.adjust(1).as_markup()

def back_to_catalog():
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='back_to_catalog'))

    return keyboard.adjust(1).as_markup()

