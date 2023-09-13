from aiogram import types
from data.models.model import ModelConnect
from states.states import UserProcess

async def Start(message: types.Message):
    mdConnect = ModelConnect()
    await mdConnect.ADDuser(message)
    await message.answer(f"привет  {message.from_user.first_name}")
    await UserProcess.defaultState.set()