from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import bot
from src.keyboards.keyboard_func import CheckData

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd1(message: Message):
    await message.answer("Botimizga xush kelibsiz, kayp qilish uchun admin bilan bog'laning!\n\n@adkhambek_4", parse_mode="html")


@user_router.message(F.chat.type == ChatType.PRIVATE)
async def enter_direction(message: Message):
    check_status, channels = await CheckData.check_member(bot, message.from_user.id)
    if check_status:
        await message.answer("<b>kayp qilish uchun admin bilan bog'laning</b>", parse_mode="html")
    else:
        await message.answer("❗ Iltimos, quyidagi kanallarga a’zo bo‘ling:",
                             reply_markup=await CheckData.channels_btn(channels))