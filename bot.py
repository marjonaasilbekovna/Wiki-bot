import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from wiki import wiki

dp = Dispatcher()

TOKEN = "7181305178:AAEVp764bS7csy8A7lcAXUrNkj7Z9x--2hE"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

@dp.message(F.text)
async def wiki_handler(message: Message):
    text = message.text

    malumot = wiki(text)
    await message.answer(malumot)
    # await massage.reply()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
