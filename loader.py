import handlers
from config import dp
from aiogram import executor


async def on_startup(dp):
    print('Starting bot')
    

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
