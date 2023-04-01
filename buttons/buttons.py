from aiogram import types
from aiogram.types import ReplyKeyboardMarkup


def create_exit_button():
    """Кнопка для выхода из режимов prompt"""

    # creating button
    exit_button = types.InlineKeyboardButton(text='Выйти из режима')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(exit_button)
    return keyboard
