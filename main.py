import openai
import aiogram
import config as cfg
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode, ChatActions, Message

# Set up OpenAI API key
openai.api_key = cfg.AI_TOKEN

# Set up Telegram bot
bot = Bot(cfg.TG_TOKEN)
dp = Dispatcher(bot)

print('mvd')

messages_arr=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "hello i am a new gpt user"},
        {"role": "assistant", "content": "Greetings! How can i help you?"},
    ]

def update(messages, role, content):
    messages_arr.append({"role": role, "content": content})
    return messages_arr


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id,"Привет! Я молодой чат бот основанный на нейросети GPT от компании OpenAI.",  parse_mode="MarkdownV2")
    await bot.send_message(message.chat.id,"Как я могу вам помочь?",  parse_mode="MarkdownV2")

@dp.message_handler()
async def respond_to_question(message: types.Message):

    update(messages_arr, "user", message.text)

    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)

    # Get the question from the user
    question = message.text

    # Call OpenAI's GPT-3 API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages_arr
    )

    # Get the best answer from the API response
    answer = response['choices'][0]['message']['content']

    # If the answer contains code, output it as a code block
    if "```" in answer:
        code = answer.replace("```", "")
        await bot.send_message(message.chat.id, text=f"```\n{code}\n```", parse_mode="MarkdownV2")

    else:
        await bot.send_message(message.chat.id, text = answer)

    await bot.send_message(message.chat.id, len(messages_arr))

    #обновление массива контекста
    update(messages_arr, "assistant", answer)

    # проверка длины контекста и орезка 

if len(messages_arr) >=16:
    messages_arr = messages_arr[:3]    




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
