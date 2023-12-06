import config as cfg
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher


# Set up Telegram bot
bot = Bot(cfg.TG_TOKEN)


"""Greeting part"""


async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Привет\! Это бот, основанный на нейросети GPT от компании OpenAI\.",
                           parse_mode="MarkdownV2")
    await bot.send_message(message.chat.id,
                           "Над разработкой трудились в крови и поте два Александра",
                           parse_mode="MarkdownV2")
    await bot.send_message(message.chat.id, "Никаких ограничений у этого бота нет, вы можете делать столько запросов, сколько пожелаете\\.  ",
                            parse_mode="MarkdownV2")
    await bot.send_message(message.chat.id,
                           "Будем очень признательный, если вы поддержите бота рублем, так как сервер и сама нейросеть убрали бесплатный период\\. В описании бота есть контакты\\)",
                            parse_mode="MarkdownV2")

def register_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])

