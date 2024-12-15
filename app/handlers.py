from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=kb.posts())


@router.message(Command('help'))
async def handle_help(message: Message):
    await message.answer('вы нажали на команду help')


@router.callback_query(F.data == 'news')
async def handle_news(callback: CallbackQuery):
    await callback.message.answer('Вы нажали на кнопку "Новости"', reply_markup=kb.news)


@router.callback_query(F.data == 'main')
async def handle_news(callback: CallbackQuery):
    await callback.message.answer('Вы нажали на кнопку "Главная"')


@router.callback_query(F.data == 'help')
async def handle_news(callback: CallbackQuery):
    await callback.message.answer('Вы нажали на кнопку "Помощь"')


@router.callback_query(F.data == 'welcome')
async def handle_game(callback: CallbackQuery):
    await callback.message.reply('Вы нажали на кнопку "Игра"')


@router.callback_query(F.data == 'monday')
async def handle_monday(callback: CallbackQuery):
    schedule = [
        {
           "title": "Понедельник",
           "subjects": [
               {
                   "name": "Математика",
                   "time": '08:00 - 08:45'
               },
               {
                   "name": "Русский язык",
                   "time": '08:00 - 08:45'
               },
               {
                   "name": "Физики",
                   "time": '08:00 - 08:45'
               },
               {
                   "name": "Литература",
                   "time": '08:00 - 08:45'
               },
           ]
        },
        {
            "title": "Вторник",
            "subjects": [
                {
                    "name": "Математика",
                    "time": '08:00 - 08:45'
                },
                {
                    "name": "Русский язык",
                    "time": '08:00 - 08:45'
                },
                {
                    "name": "Физики",
                    "time": '08:00 - 08:45'
                },
                {
                    "name": "Литература",
                    "time": '08:00 - 08:45'
                },
            ]
        }
    ]

    await callback.message.answer('1) 08:00-08:45  -  Математика\n2) 08:50-09:35  -  Русский язык\n3) 09:40-10:25  -  География\n4) 10:35-11:20  -  Литература')