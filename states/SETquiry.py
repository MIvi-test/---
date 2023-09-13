from aiogram import types
from loader import dp
from aiogram.types.callback_query import *


@dp.callback_query_handler()
async def echo(call: CallbackQuery, message:types.Message): 
    print(call.id)
    print(call.from_user.id)
    print(call.inline_message_id) 
    try:
        print(message.chat.id)
        message.answer("hay bro")
    except:
        pass
@dp.message_handler()
async def ech(message: types.Message):
    await message.answer("")