import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from src.db.connects import db
from src.db.init_db import create_tables
from src.handlers.admin import admin_router
from src.handlers.users import user_router
from src.handlers.groups import group_router
from src.handlers.channels import channel_router
from src.handlers.other import other_router
from src.middlewares.middleware import RegisterUserMiddleware


async def on_startup() -> None:
    await db.connect()
    await create_tables()


async def main():
    await on_startup()
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.update.middleware(RegisterUserMiddleware())

    dp.include_router(admin_router)
    dp.include_router(user_router)
    dp.include_router(group_router)
    dp.include_router(channel_router)
    dp.include_router(other_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())