from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import create_engine

from bot.handlers.user import user_router

from fluentogram import TranslatorHub

from config import Config, load_config
from sqlalchemy.ext.asyncio import async_sessionmaker

from bot.middlewares.db_session import DbSessionMiddleware
from bot.middlewares.i18n import TranslatorRunnerMiddleware

from bot.utils.i18n import create_translator_hub

async def main(
        config: Config,
        session_factory: async_sessionmaker
        ) -> None:
    
    translator_hub: TranslatorHub = create_translator_hub()
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.update.outer_middleware(DbSessionMiddleware(session_factory))
    dp.update.middleware(TranslatorRunnerMiddleware())
    dp.include_routers(user_router)

    await dp.start_polling(bot, _translator_hub=translator_hub)