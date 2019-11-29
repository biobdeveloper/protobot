from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup


class UserState(StatesGroup):
    start = State()
    some = State()


class AdminState(StatesGroup):
    admin = State()
