
import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "TELEGRAM_BOT_TOKEN is not configured"
    )

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Services"),
            KeyboardButton(text="🛒 New Order"),
        ],
        [
            KeyboardButton(text="📦 My Orders"),
            KeyboardButton(text="💰 Add Funds"),
        ],
        [
            KeyboardButton(text="👨‍💻 Support"),
        ],
    ],
    resize_keyboard=True,
)

@dp.message(CommandStart())
async def start(message: Message):
    name = message.from_user.first_name or "User"

    await message.answer(
        f"✦ Welcome, {name}! ✦\n\n"
        "🚀 𝐎𝐑𝐈𝐎𝐍 𝐒𝐌𝐌 𝐏𝐀𝐍𝐄𝐋 𝐒𝐄𝐑𝐕𝐈𝐂𝐄\n\n"
        "Choose an option below to get started.",
        reply_markup=menu,
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
