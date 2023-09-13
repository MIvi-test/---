from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def setReplyKeybord():
    help_keybord = ReplyKeyboardMarkup(
        reply_keyboard = 
    [
        [
            KeyboardButton(text='text', callback_data='callback')
        ],
        [
            KeyboardButton(text='text', callback_data='callback')
        ],
        [
            KeyboardButton(text='text', callback_data='callback')
        ]
    ]
    )
    return help_keybord

def setAdminReplyKeybord():
    adminKeyboard = ReplyKeyboardMarkup(
        keyboard = 
    [
        [
            KeyboardButton(text='забанить', callback_data='banUser')
        ],
        [
            KeyboardButton(text='пополнить баланс', callback_data='topUpBalance')
        ],
        [
            KeyboardButton(text='статистика', callback_data='statistics')
        ]
    ],
    resize_keyboard = True
    )
    return adminKeyboard