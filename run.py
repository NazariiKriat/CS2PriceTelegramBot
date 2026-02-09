import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from config import TOKEN
import logging
from webscrappers.webscrapper_master import run_parser
#from webscrappers.webscrapper_master_sql import run_parser             for sql



bot = Bot(token=TOKEN)
dp = Dispatcher()

async def parser_loop():
    while True:
        try:
            print("⏳ Starting scheduled parser run")
            await asyncio.to_thread(run_parser)
        except Exception as e:
            print("❌ Parser error:", e)

        await asyncio.sleep(120)  # 5 minutes

async def main():
    dp.include_router(router)
    asyncio.create_task(parser_loop())
    
    await dp.start_polling(bot)
    



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
