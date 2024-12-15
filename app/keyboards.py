from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import requests

menu_reply_markup = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Главная'), KeyboardButton(text='Новости')],
    [KeyboardButton(text='Помощь')],
], resize_keyboard=True)

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Главная', callback_data='main'), InlineKeyboardButton(text='Новости', callback_data='news')],
    [InlineKeyboardButton(text='Помощь', callback_data='help'), InlineKeyboardButton(text='Игра', callback_data='game')]
])

news = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Погода', callback_data='weather'), InlineKeyboardButton(text='Бизнесс', callback_data='business')],
    [InlineKeyboardButton(text='Игры', callback_data='game'), InlineKeyboardButton(text='Ютуб', callback_data='youtube')],
    [InlineKeyboardButton(text='Музыка', callback_data='music'), InlineKeyboardButton(text='Технологии', callback_data='technologies')]
])

schedule = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Расписание на понедельник', callback_data='monday')]
])

def posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    keyboard = InlineKeyboardBuilder()

    for post in posts:
        keyboard.add(InlineKeyboardButton(text=post['title'][:10], callback_data=str(post['id'])))

    return keyboard.adjust(5).as_markup()
