from aiogram.dispatcher.filters.state import StatesGroup, State


class GenerateText(StatesGroup):
    cmd_generate = State()
    wait_prompt = State()


""" class GenerateImage(StatesGroup):
    cmd_generate = State()
    wait_prompt = State()
 """