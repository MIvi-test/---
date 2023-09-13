from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminProcess(StatesGroup):
    adminMode = State()
    banUsers = State()
    saveUsername = State()
    saveMoney = State()
    
class UserProcess(StatesGroup):
    defaultState = State()
    gameState = State()
    gameTrying = State()
    