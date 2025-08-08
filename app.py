import asyncio

from config import Config, load_config
from bot.bot import main

from bot.database.init_db import create_engine_and_session, init_db

config: Config = load_config()

async def startup():
    config = load_config()
    engine, session_factory = await create_engine_and_session(config)
    await(init_db(engine))
    await(main(config, session_factory))

asyncio.run(startup())