
from data.config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(token=TOKEN)
memory = MemoryStorage()
dp = Dispatcher(bot, storage=memory)
