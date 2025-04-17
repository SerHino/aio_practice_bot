from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove
from aiogram import executor
from logging import basicConfig, INFO

from data.config import ADMINS
from loader import dp, db, bot

import handlers


user_message = 'Користувач'
admin_message = 'Адмін'
ADMIN_PASSWORD = 'aboba'

user_states = {}


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row(user_message, admin_message)

    await message.answer('''Привіт! 👋

🤖 Я бот-магазин з продажу товарів будь-якої категорії.

🛍️ Щоб перейти до каталогу і вибрати цікаві вам 
товари скористайтесь командою /menu.

❓ Виникли питання? Це не проблема! Команда /sos допоможе 
зв'язатися з адмінами, які постараються якнайшвидше відгукнутися.
    ''', reply_markup=markup)


@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):
    cid = message.chat.id
    if cid not in ADMINS:
        await message.answer("Будь-ласка, введіть пароль для доступу до режиму адміністратора:")
        user_states[cid] = "awaiting_password"


@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):
    cid = message.chat.id
    if cid in ADMINS:
        ADMINS.remove(cid)

    await message.answer('Ввімкнений режим користувача.',
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def handle_password(message: types.Message):
    cid = message.chat.id

    if user_states.get(cid) == "awaiting_password":
        if message.text == ADMIN_PASSWORD:
            ADMINS.append(cid)
            await message.answer("Пароль вірний! Ввімкнений режим адміністратора.", reply_markup=ReplyKeyboardRemove())
        else:
            await message.answer("Невірний пароль! Спробуйте ще раз.")

        user_states.pop(cid, None)

async def on_startup(dp):
    basicConfig(level=INFO)
    db.create_tables()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
