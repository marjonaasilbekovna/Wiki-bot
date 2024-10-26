from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💁🏻‍♂️ Bot haqida"), KeyboardButton(text="📥Send message admin")],
        [KeyboardButton(text="☎️ Contact admin")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Quyidagi tugmalardan birini tanlang..."
)
