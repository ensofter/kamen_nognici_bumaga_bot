from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def handle_every_message(message: Message):
    await message.answer('Ответ на любой твой вопрос')