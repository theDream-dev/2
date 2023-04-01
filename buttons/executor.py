from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery


import config as cfg

bot = Bot(cfg.TG_TOKEN)
dp = Dispatcher(bot)


async def process_button(callback_query: CallbackQuery, state: FSMContext):
    # Получаем данные, которые были переданы в кнопке
    data = callback_query.data

    if data == 'Exit mode':
        await callback_query.message.answer("Exit mode")

        await state.finish()
        await callback_query.answer()


