import logging

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU
import logging


logger = logging.getLogger(__name__)

button_yes = KeyboardButton(text=LEXICON_RU['accept_button_yes'])
button_no = KeyboardButton(text=LEXICON_RU['refuse_button_no'])

accept_refuse_game_keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_yes],
    [button_no]
],
    one_time_keyboard=True,
    resize_keyboard=True
)


button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])

chose_instrument_keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_rock],
    [button_scissors],
    [button_paper]
],
    one_time_keyboard=True,
    resize_keyboard=True
)
