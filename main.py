from core.config import TOKEN

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from hendlers.filter_hendler import Filter
from hendlers.weather_hendler import WeatherHendler
from hendlers.menu_hendler import MenuHendler
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initilize Storage
storage = MemoryStorage()
# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

MenuHendler(bot, dp, types=types)
WeatherHendler(bot, dp, types=types, fsm_context=FSMContext)
Filter(dp, types=types)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


