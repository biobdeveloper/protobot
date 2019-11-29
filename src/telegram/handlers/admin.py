from aiogram import types

from src.app import bot, dp
from src.text_content import AdminTextMessage
from src.telegram.states import AdminState


@dp.message_handler(commands=['admin'], state='*')
async def admin(message: types.Message):
    await bot.s_send_message(AdminTextMessage.start.format(message.from_user.id))
    await AdminState.admin.set()
