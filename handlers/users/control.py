from time import sleep
from aiogram import types
from states import states
from loader import dp



@dp.message_handler(commands = ['game','play', 'игра'], state= states.UserProcess.defaultState)
async def FirstForeword(message:types.Message):
    await message.answer("привет, это игра на удачу, у вас примерно 50% чтобы победить,"
                         f"{message.from_user.first_name}, мы верим в вашу удачу")
    await message.answer("напиши /ПОГНАЛИ, если готовы пытаться")
    await states.UserProcess.gameState.set()
    
@dp.message_handler(commands = ['правила', 'rules'], state=states.UserProcess.gameState)
async def rulesFirstGame(message: types.Message):
    await message.answer("наша гениальная программа загадывает РАНДОМНОЕ число от 1 до 100, ваша задача отгадать, данное число удачи")
    sleep(2)
    await message.answer("напиши /ПОГНАЛИ, если готовы пытаться")
    
@dp.message_handler(commands=['ПОГНАЛИ', 'погнали'], state=states.UserProcess.gameState)
async def kkk(message:types.Message):
    await message.answer("мы загадали число, пробуйте отгадать!!")
    #смена state на попытку отгадать
    await states.UserProcess.gameTrying.set()


@dp.message_handler(state=states.UserProcess.gameTrying)
async def FirstGameStart(message : types.Message):
    attempt = None # из базы данных
    secretNumber = None
    if message.text.isnumeric():
        if attempt > 0:
            attempt -= 1 # запрос в базу данных
            await message.answer(f"у вас осталось {attempt} попыток.")
            if int(message.text) > secretNumber:
                message.answer("твоё число больше чем загаданное, try again")
            elif int(message.text )< secretNumber:
                message.answer("твоё число меньше загаданного, try again")
            elif int(message.text) == secretNumber:
                message.answer("Вы выиграли!!! ")
                #здесь нужны умные сбросы состояний, выдача приза, и рессет в базе
    else:
        message.answer("no valid, only numbers")        
        
        