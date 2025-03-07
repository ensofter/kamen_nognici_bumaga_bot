import random

from lexicon.lexicon_ru import LEXICON_RU


def random_answer():
    bot_choice = random.choice([LEXICON_RU['rock'], LEXICON_RU['scissors'], LEXICON_RU['paper']])
    return bot_choice


def who_is_win(user_choice: str, bot_choice):
    if user_choice == f'{LEXICON_RU["rock"]}' and bot_choice == f'{LEXICON_RU["paper"]}':
        return "bot_won"
    if user_choice == f'{LEXICON_RU["rock"]}' and bot_choice == f'{LEXICON_RU["scissors"]}':
        return "user_won"
    if user_choice == f'{LEXICON_RU["scissors"]}' and bot_choice == f'{LEXICON_RU["rock"]}':
        return "bot_won"
    if user_choice == f'{LEXICON_RU["scissors"]}' and bot_choice == f'{LEXICON_RU["paper"]}':
        return "user_won"
    if user_choice == f'{LEXICON_RU["paper"]}' and bot_choice == f'{LEXICON_RU["scissors"]}':
        return "bot_won"
    if user_choice == f'{LEXICON_RU["paper"]}' and bot_choice == f'{LEXICON_RU["rock"]}':
        return "user_won"
    if user_choice == bot_choice:
        return "nobody_won"
