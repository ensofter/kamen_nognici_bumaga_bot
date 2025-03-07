import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import load_config

from handlers import other_handlers
from handlers import user_handlers
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


logger = logging.getLogger(__name__)


async def main():
    tg_config = load_config()
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] - %(levelname)-8s %(filename)s:%(lineno)d '
                                                    '%(name)s - %(message)s')

    bot = Bot(
        token=tg_config.tg.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
