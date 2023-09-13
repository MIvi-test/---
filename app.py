from aiogram import executor,types
from loader import dp,bot
from handlers.users.start import Start
from handlers.admin.adminMode import FuncAdmins
from utils import *
from keyboards import *
from states import SETquiry
from aiogram.types.callback_query import CallbackQuery 



@dp.message_handler(commands=['start'])
async def StartCommand(message: types.Message):
    await Start(message=message)

@dp.message_handler()
async def Nocommand(message:types.Message):
        await message.answer("команда не распознана")                    

if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)
else:
        executor.start_polling(dp)