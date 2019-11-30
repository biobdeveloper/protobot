from src.database import Connector

conn = Connector()


async def register(user):
    conn.add_new_telegram_user(**dict(user))


async def add_new_backend_data(user, data):
    conn.add_new_backend_data(user, data)


async def get_backend_data(user):
    return conn.get_backend_data(user)
