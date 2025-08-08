from dataclasses import dataclass
from environs import Env

@dataclass
class BotSettings:
    token: str
    admin_ids: list[int]

@dataclass
class DbConfig:
    dsn: str

@dataclass
class Config:
    bot: BotSettings
    db: DbConfig

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    token = env("BOT_TOKEN")
    admin_ids = env.list('ADMIN_IDS', subcast=int)
    dsn = env("DB_DSN")
    return Config(
        bot=BotSettings(token=token, admin_ids=admin_ids),
        db=DbConfig(dsn=dsn)
    )