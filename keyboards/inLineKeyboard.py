from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def setUserKeyboard():
    userKeyboard = InlineKeyboardMarkup(
        inline_keyboard = 
    [
        [
            InlineKeyboardButton(text='text', callback_data='callback')
        ],
        [
            InlineKeyboardButton(text='text', callback_data='callback')
        ],
        [
            InlineKeyboardButton(text='text', callback_data='callback')
        ]
    ]
    )
    return userKeyboard



def setAdminKeyboard():
    adminKeboard= InlineKeyboardMarkup(
        inline_keyboard = 
    [
        [
            InlineKeyboardButton(text='забанить', callback_data='banUser')
        ],
        [
            InlineKeyboardButton(text='пополнить баланс', callback_data='topUpBalance')
        ],
        [
            InlineKeyboardButton(text='статистика', callback_data='statistics')
        ]
    ]
    )
    return adminKeboard