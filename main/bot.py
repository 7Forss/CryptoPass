from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import logging
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в CryptoPassport! Используйте /webapp чтобы запустить приложение.")

@dp.message_handler(commands=['webapp'])
async def webapp(message: types.Message):
    await message.answer("Нажмите на кнопку ниже для запуска Web App", reply_markup=types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("Open Web App", web_app=types.WebAppInfo(url="http://localhost:5000/static/index.html"))
    ))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)