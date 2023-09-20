from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_cats_markup(cats) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="1"))
    kb.add(KeyboardButton(text="2"))
    kb.add(KeyboardButton(text="3"))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard = True)



