from aiogram import types

from src.app import bot, dp
from src.text_content import TextMessage
from src.backend.__init__ import *
from src.telegram.states import UserState
from src.telegram.keyboards import keyboards


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    await bot.s_send_message(TextMessage.start, reply_markup=keyboards['start'])
    await register(message.from_user)
    await UserState.start.set()


@dp.message_handler(commands=['add'], state=UserState.start)
async def add_new_user_data(message: types.Message):
    data = message.text.split()[1]
    await add_new_backend_data(message.from_user, data)
    await bot.s_send_message(TextMessage.add_new_user_data)


@dp.message_handler(commands=['get'], state=UserState.start)
async def get_user_data(message: types.Message):
    data = await get_backend_data(message.from_user)
    await bot.s_send_message(TextMessage.get_user_data.format(data))

