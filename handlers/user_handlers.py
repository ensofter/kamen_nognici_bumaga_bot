import logging

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards.keyboards import yes_no_kb, chose_instrument_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from services.services import random_answer, who_is_win

router = Router()

logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def handle_cmd_start(message: Message):
    await message.answer(text=LEXICON_RU['start'], reply_markup=yes_no_kb)


@router.message(Command(commands=['help']))
async def handle_cmd_help(message: Message):
    await message.answer(text=LEXICON_RU['help'], reply_markup=yes_no_kb)


@router.message(F.text == LEXICON_RU['accept_button_yes'])
async def handle_gema_accept(message: Message):
    await message.answer(text=LEXICON_RU['game_accept'], reply_markup=chose_instrument_keyboard)


@router.message(F.text == LEXICON_RU['refuse_button_no'])
async def handle_gema_accept(message: Message):
    await message.answer(text=LEXICON_RU['game_refuse'])


@router.message(F.text.in_([LEXICON_RU['rock'], LEXICON_RU['scissors'], LEXICON_RU['paper']]))
async def handle_user_answer(message: Message):
    bot_answer = random_answer()
    await message.answer(text=f"{LEXICON_RU['bot_choice']} - {bot_answer}")
    who_win = who_is_win(message.text, bot_answer)
    await message.answer(text=LEXICON_RU[who_win], reply_markup=yes_no_kb)