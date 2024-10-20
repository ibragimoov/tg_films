from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb

router = Router()

'''
Задание:
1) обработать нажатие на кнопку "Главная" - "Вы нажали на кнопку "Главная""
2) обработать нажатие на кнопку "Помощь" - "Вы нажали на кнопку "Помощь""
3) создать клавиатуру Inline - произвольную
4) вывести клавиатуру к сообщению из задания 1)
'''

@router.message(CommandStart())
async def handle_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=kb.menu)
@router.callback_query(F.data == 'news')
async def handle_news(callback: CallbackQuery):
    await callback.message.answer('Вы нажали на кнопку "Новости"', reply_markup=kb.news)

@router.callback_query(F.data == 'main')
async def handle_news(callback: CallbackQuery):
    await callback.message.answer('Вы нажали на кнопку "Главная"')

@router.callback_query(F.data == 'help')
async def handle_news(callback: CallbackQuery):
    await callback.message.answer('Вы нажали на кнопку "Помощь"')