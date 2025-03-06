import random


def random_answer():
    bot_choice = random.choice(['камень', 'ножницы', 'бумага'])
    return bot_choice


def who_is_win(user_choice: str, bot_choice):
    if user_choice == 'камень' and bot_choice == 'бумага':
        return 'Бот победил!'
    if user_choice == 'камень' and bot_choice == 'ножницы':
        return 'Ты победил!'
    if user_choice == 'ножницы' and bot_choice == 'камень':
        return 'Бот победил!'
    if user_choice == 'ножницы' and bot_choice == 'бумага':
        return 'Ты победил!'
    if user_choice == 'бумага' and bot_choice == 'ножницы':
        return 'Бот победил!'
    if user_choice == 'бумага' and bot_choice == 'камень':
        return 'Бот победил!'
    if user_choice == bot_choice:
        return 'Ничья'
