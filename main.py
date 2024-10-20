import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main():
    bot = Bot(token='8101609114:AAGEMmGwCm3m-SQ70jYQwVtayd2N8Wk0qBY')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())