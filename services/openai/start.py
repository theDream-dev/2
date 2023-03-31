import openai
import requests

import config as cfg
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode, ChatActions, Message


# Set up Telegram bot
bot = Bot(cfg.TG_TOKEN)


"""Greeting part"""


async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Привет\! Это новый бот, основанный на нейросети GPT от компании OpenAI\.",
                           parse_mode="MarkdownV2")
    await bot.send_message(message.chat.id,
                           "Над разработкой трудились в крови и поте два Александра \- некие Руденко и Шмигельский",
                           parse_mode="MarkdownV2")
    await bot.send_message(message.chat.id, "Чем я могу Вам помочь?", parse_mode="MarkdownV2")


def register_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])

