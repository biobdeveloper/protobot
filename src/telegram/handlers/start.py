from aiogram import types

from src.app import bot, dp
from src.text_content import TextMessage
from src.backend.backend import register
from src.telegram.states import UserState
from src.telegram.keyboards import keyboards


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    await bot.s_send_message(TextMessage.start, reply_markup=keyboards['start'])
    await register(message.from_user)
    await UserState.start.set()
