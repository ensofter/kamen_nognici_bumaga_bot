import logging

from aiogram.types import BotCommand
from aiogram import Bot

from lexicon.lexicon_ru import LEXICON_COMMANDS_RU

logger = logging.getLogger(__name__)

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=k, description=v) for k, v in LEXICON_COMMANDS_RU.items()
    ]

    await bot.set_my_commands(main_menu_commands)
