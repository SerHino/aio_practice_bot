from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from keyboards.default.markups import all_right_message, cancel_message, submit_markup
from aiogram.types import Message
from states import SosState
from filters import IsUser
from loader import dp, db


@dp.message_handler(commands='sos')
async def cmd_sos(message: Message):
    await SosState.question.set()
    await message.answer(
        'У чому суть проблеми? Опишіть якомога детальніше'
        ' та адміністратор обов`язково вам відповість.',
        reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=SosState.question)
async def process_question(message: Message, state: FSMContext):
    async with state.proxy()as data:
        data['question'] = message.text

    await message.answer('Переконайтеся, що все правильно.',
                         reply_markup=submit_markup())
    await SosState.next()
@dp.message_handler(
    lambda message: message.text not in [cancel_message, all_right_message],
    state=SosState.submit)
async def process_price_invalid(message: Message):
    await message.answer('Такого варіанта не було.')


@dp.message_handler(text=cancel_message, state=SosState.submit)
async def process_cancel(message: Message, state: FSMContext):
    await message.answer('Скасовано!', reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text=all_right_message, state=SosState.submit)
async def process_submit(message: Message, state: FSMContext):
    cid = message.chat.id

    if db.fetchone('SELECT * FROM questions WHERE cid=?', (cid,)) is None:

        async with state.proxy() as data:
            db.query('INSERT INTO questions VALUES (?, ?)',
                     (cid, data['question']))

        await message.answer('Відправленно!', reply_markup=ReplyKeyboardRemove())

    else:

        await message.answer(
            'Перевищено ліміт на кількість запитань.',
            reply_markup=ReplyKeyboardRemove())

    await state.finish()


