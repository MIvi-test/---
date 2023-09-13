from time import sleep
from aiogram import types
from data.models import model
from states import states
from loader import dp
from keyboards.ReplyKeyboard import setAdminReplyKeybord
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands=['adminMode', 'admin'])
async def ADMINmode(message: types.Message):
        if message.from_user.username == "OnlyFunForYou":
                await FuncAdmins(message=message)
                await states.AdminProcess.adminMode.set()
        else:
                await message.answer("неизвестная команда")
  
  
@dp.message_handler(commands=['noadmin', 'noAdmin', 'stopAdmin', 'stopadmin'], state= states.AdminProcess.adminMode) 
async def ressetAdminMode(message:types.Message):
        await states.UserProcess.defaultState.set()
        states.AdminProcess.adminMode.set().close()
               
    
    
@dp.message_handler(state=states.AdminProcess.adminMode)
async def tr(message: types.Message):
        await message.answer("окей, пробуем")
        sleep(1)
        match message.text:
                case "забанить":
                        pass
                
                case "пополнить баланс":
                        await  message.answer("скидывай username")
                        await states.AdminProcess.saveUsername.set()
                        
                case "статистика":
                        pass
    

@dp.message_handler(state=states.AdminProcess.saveUsername)
async def replenishBalance(message:types.Message,state: FSMContext):
        state.update_data(username=message.text)
        await message.answer("кидай на сколько ты хочешь ему пополнить кошелек")
        states.AdminProcess.saveMoney.set()
        
@dp.message_handler(state=states.AdminProcess.saveMoney)
async def replenishBalance(message:types.Message, state: FSMContext):
        state.update_data(money=message.text)
        data = state.get_data()
        conn = model.ModelConnect()
        print(data)
        conn.ADDbalance(username = data["username"], money=data["money"])
        state.reset_data()
        states.AdminProcess.adminMode.set()

   
@dp.message_handler(state= states.UserProcess.defaultState)
async def defoult(message:types.Message):
        await message.answer("problem defolt")






async def FuncAdmins(message: types.Message):
    await message.answer("YOU START admin's Mode")
    sleep(1)
    await message.answer("что вы хотите?", reply_markup=setAdminReplyKeybord())
    