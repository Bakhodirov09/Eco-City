from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext

from keyboards.default.default_keyboards import main_menu
from loader import dp, _
from utils.db_api.database_functions import add_user


@dp.message_handler(state='*', commands='start')
async def bot_start(message: types.Message, state: FSMContext):
    userga = _(f"Assalomu alaykum ")
    userga += message.from_user.full_name
    userga += _(f" botimizga xush kelibsiz.")
    await add_user(full_name=message.from_user.full_name, chat_id=message.chat.id, lang=types.User.language_code)
    await message.answer(text=userga, reply_markup=await main_menu(lang=types.User.language_code if types.User.language_code in ['ru', 'uz'] else 'uz'))
    await state.set_state('in_start')