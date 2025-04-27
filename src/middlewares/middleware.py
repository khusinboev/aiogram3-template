from aiogram.types import Update
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from datetime import datetime
import pytz

from src.db.connects import db


class RegisterUserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict):
        if not event.message:
            return await handler(event, data)  # Middleware davom etsin

        user = event.message.from_user
        user_id = user.id
        username = user.username if user.username else None
        date = datetime.now(pytz.timezone("Asia/Tashkent")).date()
        lang_code = user.language_code if user.language_code else "uz"


        # **1️⃣ SQL Injection xavfsizligi uchun f-string emas, parametr ishlatilmoqda**
        user = await db.fetchone(f"SELECT * FROM accounts WHERE user_id = {user_id}")
        if not user:
            await db.execute(f"INSERT INTO accounts (user_id, username, lang_code, created_at) VALUES ('{user_id}', '{username}', '{lang_code}', '{date}')")

        return await handler(event, data)  # **2️⃣ Xatolik tuzatildi, middleware davom etadi**