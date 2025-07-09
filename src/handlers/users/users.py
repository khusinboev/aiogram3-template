from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd1(message: Message):
    await message.answer("Botimizga xush kelibsiz, kayp qilish uchun admin bilan bog'laning!\n\n@adkhambek_4", parse_mode="html")
