import logging

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards.keyboards import accept_refuse_game_keyboard, chose_instrument_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from services.services import random_answer, who_is_win

router = Router()

logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def handle_cmd_start(message: Message):
    await message.answer(LEXICON_RU['start'], reply_markup=accept_refuse_game_keyboard)


@router.message(Command(commands=['help']))
async def handle_cmd_help(message: Message):
    await message.answer(LEXICON_RU['help'])


@router.message(F.text.lower() == 'давай!')
async def handle_gema_accept(message: Message):
    await message.answer(text=LEXICON_RU['game_accept'], reply_markup=chose_instrument_keyboard)


@router.message(F.text.lower() == 'не хочу!')
async def handle_gema_accept(message: Message):
    await message.answer(text=LEXICON_RU['game_refuse'], reply_markup=chose_instrument_keyboard)


@router.message(F.text.lower().in_(['камень', 'ножницы', 'бумага']))
async def handle_user_answer(message: Message):
    bot_answer = random_answer()
    logger.info(bot_answer)
    await message.answer(text=f'Ответ бота\n{bot_answer}')
    who_win = who_is_win(message.text.lower(), bot_answer)
    logger.info(who_win)
    await message.answer(text=who_win)