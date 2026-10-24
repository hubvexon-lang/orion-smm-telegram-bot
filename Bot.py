
import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

# Configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "TELEGRAM_BOT_TOKEN environment variable is missing."
    )

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Main menu
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
            KeyboardButton(text="👤 My Account"),
            KeyboardButton(text="👨‍💻 Support"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose an option...",
)

# Start command
@dp.message(CommandStart())
async def start(message: Message):
    name = message.from_user.first_name or "User"

    await message.answer(
        f"✦ Welcome, {name}! ✦\n\n"
        "🚀 𝐎𝐑𝐈𝐎𝐍 𝐒𝐌𝐌 𝐏𝐀𝐍𝐄𝐋 𝐒𝐄𝐑𝐕𝐈𝐂𝐄\n\n"
        "Welcome to our SMM service panel.\n"
        "Choose an option from the menu below.",
        reply_markup=menu,
    )

# Help command
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Use the menu buttons to navigate the panel.\n"
        "For assistance, select 👨‍💻 Support."
    )

# Menu buttons
@dp.message(F.text == "📋 Services")
async def services(message: Message):
    await message.answer(
        "📋 Services\n\n"
        "Services will appear here after the provider API "
        "is configured."
    )

@dp.message(F.text == "🛒 New Order")
async def new_order(message: Message):
    await message.answer(
        "🛒 New Order\n\n"
        "Order placement will be enabled after service "
        "selection, balance checks, and API setup."
    )

@dp.message(F.text == "📦 My Orders")
async def my_orders(message: Message):
    await message.answer(
        "📦 My Orders\n\n"
        "Your order history will appear here after the "
        "database connection is configured."
    )

@dp.message(F.text == "💰 Add Funds")
async def add_funds(message: Message):
    await message.answer(
        "💰 Add Funds\n\n"
        "Add Funds requests are handled manually by the admin.\n"
        "Please contact support for payment instructions."
    )

@dp.message(F.text == "👤 My Account")
async def my_account(message: Message):
    user = message.from_user

    await message.answer(
        "👤 My Account\n\n"
        f"Telegram ID: {user.id}\n"
        f"Username: @{user.username}"
        if user.username
        else f"👤 My Account\n\nTelegram ID: {user.id}\nUsername: Not set"
    )

@dp.message(F.text == "👨‍💻 Support")
async def support(message: Message):
    await message.answer(
        "👨‍💻 Support\n\n"
        "Please contact the panel administrator for help."
    )

# Run bot
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
