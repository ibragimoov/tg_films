from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import requests
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.menu)

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('каталог книг', reply_markup=kb.books())

@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.message.edit_text('Добро пожаловать!', reply_markup=kb.menu)


@router.callback_query(F.data == 'back_to_catalog')
async def back(callback: CallbackQuery):
    await callback.message.edit_text('каталог книг', reply_markup=kb.books())


@router.callback_query(F.data.startswith('book|'))
async def book_details(callback: CallbackQuery):
    book_id = callback.data.split('|')[1]
    book_list = requests.get('https://www.googleapis.com/books/v1/volumes?q=search+terms')
    book_data = book_list.json()['items']

    founded_book = {}
    for book in book_data:
        if book['id'] == book_id:
            founded_book = book
            break

    message_text = f'{founded_book['volumeInfo']['title']}\n\n{founded_book['volumeInfo']['description'][:100]}...\n\n{founded_book['volumeInfo']['pageCount']}'

    await callback.message.edit_text(message_text, reply_markup=kb.back_to_catalog())