from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# menu = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Главная'), KeyboardButton(text='Новости')],
#     [KeyboardButton(text='Помощь')],
# ], resize_keyboard=True)

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Главная', callback_data='main'), InlineKeyboardButton(text='Новости', callback_data='news')],
    [InlineKeyboardButton(text='Помощь', callback_data='help')]
])

news = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Погода', callback_data='weather'), InlineKeyboardButton(text='Бизнесс', callback_data='business')],
    [InlineKeyboardButton(text='Игры', callback_data='game'), InlineKeyboardButton(text='Ютуб', callback_data='youtube')],
    [InlineKeyboardButton(text='Музыка', callback_data='music'), InlineKeyboardButton(text='Технологии', callback_data='technologies')]
])