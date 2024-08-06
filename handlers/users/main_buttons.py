from aiogram.dispatcher.storage import FSMContext

from keyboards.default.default_keyboards import events, problems, weeks, cancel, main_menu
from loader import dp, types, _
from utils.db_api.database_functions import get_user, add_event


@dp.message_handler(state='in_start')
async def in_start_handler(message: types.Message, state: FSMContext):
    user = await get_user(message.chat.id)
    if message.text.split(' ')[0] == "🎉":
        await message.answer(text=_(f"😊 Bo'limni tanlang", locale=user['lang']), reply_markup=await events(user['lang']))
        await state.set_state('in_events')
    elif message.text.split(' ')[0] == "❗️":
        await message.answer(text=_(f"😊 Bo'limni tanlang", locale=user['lang']), reply_markup=await problems(user['lang']))
        await state.set_state('in_problems')
    elif message.text.split(' ')[0] == "👩‍🏫":
        await message.answer(text=_(f"😊 Bo'limni tanlang", locale=user['lang']), reply_markup=await problems(user['lang']))
        await state.set_state('in_lessons')
    elif message.text.split(' ')[0] == "🌤":
        await message.answer_photo(photo="https://obhavo.uz/images/preview-logo-uz.png", caption=_("Siz qaysi kunning ob havosini bilmoqchisiz", locale=user['lang']),reply_markup=await weeks(user['lang']))
        await state.set_state('in_weather')
    elif message.text.split(' ')[0] == "⚙️":
        await message.answer(text=_(f"😊 Sizning sozlamalaringiz", locale=user['lang']))
        await state.set_state('in_settings')

@dp.message_handler(state='in_events')
async def in_events_handler(message: types.Message, state: FSMContext):
    user = await get_user(chat_id=message.chat.id)
    if message.text.split(' ')[0] == "➕🎉":
        await message.answer(text=_(f"✍️ Tadbiringiz uchun nom bering.\nMasalan: Daraxt ekish", locale=user['lang']), reply_markup=await cancel(user['lang']))
        await state.set_state('title_event')

@dp.message_handler(state='title_event')
async def title_event(message: types.Message, state: FSMContext):
    user = await get_user(message.chat.id)
    await state.update_data({
        'title': message.text
    })
    await message.answer(text=_(f"😊 Tadbiringiz haqida ma'lumot bering.\nMasalan: Siz nima maqsadda tadbir qilmoqchisiz? Shu kabi.", locale=user['lang']))
    await state.set_state('send_desc')

@dp.message_handler(state='send_desc')
async def send_desc_handler(message: types.Message, state: FSMContext):
    user = await get_user(chat_id=message.chat.id)
    await state.update_data({
        'desc': message.text
    })
    await message.answer(text=_(f"🖼 Tadbiringizni qayerda qilmoqchisiz. Joylashuvni rasmini yuboring.", locale=user['lang']))
    await state.set_state('send_photo')

@dp.message_handler(state='send_photo', content_types=types.ContentType.PHOTO)
async def send_photo_handler(message: types.Message, state: FSMContext):
    user = await get_user(chat_id=message.chat.id)
    await state.update_data({
        'photo': message.photo[-1].file_id,
        'chat_id': message.chat.id,
    })
    data = await state.get_data()
    await add_event(data=data)
    await message.answer(text=_(f"✅ Sizning tadbiringiz qoshildi.", locale=user['lang']), reply_markup=await main_menu(lang=user['lang']))
    await state.set_state('in_start')