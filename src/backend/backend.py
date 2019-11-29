from src.database import Connector

conn = Connector()


async def register(user):
    conn.add_new_telegram_user(**dict(user))
