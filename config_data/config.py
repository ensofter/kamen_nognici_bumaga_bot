from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str = None
    admins: list[int] = None


@dataclass
class TgConfig:
    tg: TgBot = None


def load_config():
    env = Env()
    env.read_env()

    return TgConfig(
        tg=TgBot(
            token=env('TG_BOT_TOKEN'),
            admins=[int(i) for i in env.list('TG_ADMINS')]
        )
    )
