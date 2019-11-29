from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup

from src.telegram.buttons import *
start = ReplyKeyboardMarkup(resize_keyboard=True)
start.row(push_me)


keyboards = {
    'start': start
}