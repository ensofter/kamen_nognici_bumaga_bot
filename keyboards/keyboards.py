import logging

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

logger = logging.getLogger(__name__)

button_yes = KeyboardButton(text=LEXICON_RU['accept_button_yes'])
button_no = KeyboardButton(text=LEXICON_RU['refuse_button_no'])

accept_refuse_game_builder = ReplyKeyboardBuilder()
accept_refuse_game_builder.row(button_yes, button_no, width=2)

yes_no_kb = accept_refuse_game_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# accept_refuse_game_keyboard = ReplyKeyboardMarkup(keyboard=[
#     [button_yes],
#     [button_no]
# ],
#     one_time_keyboard=True,
#     resize_keyboard=True
# )

button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])

chose_instrument_keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_rock],
    [button_scissors],
    [button_paper]
],
    resize_keyboard=True
)
