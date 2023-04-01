from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# create button
exit_mode = KeyboardButton('Exit mode')

# create keyboard and add button
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(exit_mode)

