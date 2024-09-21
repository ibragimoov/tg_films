from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb

import requests

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.menu)