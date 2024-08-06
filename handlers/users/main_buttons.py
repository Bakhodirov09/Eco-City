from aiogram.dispatcher.storage import FSMContext

from keyboards.default.default_keyboards import events, problems, weeks, cancel, main_menu
from loader import dp, types, _
from utils.db_api.database_functions import get_user, add_event, add_problem, get_all_problems_user, get_all_problems


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

@dp.message_handler(state='in_problems')
async def in_problems(message: types.Message, state: FSMContext):
    if message.text.split(' ')[0] == "➕":
        await message.answer(text=_(f"Shikoyatingizni yozing.", locale=types.User.language_code), reply_markup=await cancel(lang=types.User.language_code))
        await state.set_state('plus_problem')
    elif message.text.split(' ')[0] == "‼️":
        for problem in await get_all_problems_user(chat_id=message.chat.id):
            await message.answer_photo(photo=problem['photo'], caption=problem['title'], reply_markup=await main_menu('uz'))
        await state.set_state('in_start')
    elif message.text.split(' ')[0] == "❗️":
        for problem in await get_all_problems():
            await message.answer_photo(photo=problem['photo'], caption=problem['title'], reply_markup=await main_menu('uz'))
        await state.set_state('in_start')
@dp.message_handler(state='plus_problem')
async def plus_problem_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        'title': message.text
    })
    await message.answer(text=_(f"🖼 Shikoyatingiz rasmini yuboring.", locale='uz'))
    await state.set_state('send_photo')

@dp.message_handler(state='send_photo', content_types=types.ContentType.PHOTO)
async def send_photo(message: types.Message, state: FSMContext):
    await state.update_data({
        'photo': message.photo[-1].file_id,
        'chat_id': message.chat.id
    })
    data = await state.get_data()
    await add_problem(data=data)
    await message.answer(text=f"✅ Shikoyatingiz qoshildi.", reply_markup=await main_menu('uz'))



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
    
@dp.messgae_handler(state='week', text="Dushanba")
async def dushanba_function(message: types.Message, state: FSMContext):
    await message.answer("Dushanba \n\n☀️ +38°...+20°, Ochiq havo \n\nHozir: ☀️ +25°, ⬅️ 10 m/s \n\nTong: ☀️ +29° \nKun: ☀️ +36° \nOqshom: ☀️ +35° \n\nNamlik: 40% \nShamol: Sharqiy-shimoli-sharq, 9 m/s \nBosim: 758 mm sim. ust. \n\nOy: Yosh oy \nQuyosh chiqishi: 04:42 \nQuyosh botishi: 19:39", reply_markup=await main_menu('uz'))
    await state.set_state('in_start')


@dp.messgae_handler(state='week', text="Seshanba")
async def seshanba_function(message: types.Message, state: FSMContext):
    await message.answer("Seshanba \n\n☀️ +25°...+13°, Ochiq havo \n\nYog'ingarchilik ehtimoli: 6%", reply_markup=await main_menu('uz'))
    await state.set_state('in_start')

@dp.messgae_handler(state='week', text="Chorshanba")
async def chorshanba_function(message: types.Message, state: FSMContext):
    await message.answer("Seshanba \n\n☀️ +25°...+13°, Ochiq havo \n\nYog'ingarchilik ehtimoli: 6%", reply_markup=await main_menu('uz'))
    await state.set_state('in_start')

@dp.messgae_handler(state='week', text="Payshanba")
async def payshanba_function(message: types.Message, state: FSMContext):
    await message.answer("Chorshanba \n\n🌧 +28°...+13°, Yomg'ir \n\nHozir: 🌤 +16°, ↙️ 8 m/s \n\nTong: ☀️ +21° \nKun: ☀️ +27° \nOqshom: ☀️ +26° \n\nNamlik: 54% \nShamol: Shimoliy-shimoli-sharqiy, 7 m/s \nBosim: 767 mm sim. ust. \n\nOy: Qisqarayotgan oy \nQuyosh chiqishi: 04:59 \nQuyosh botishi: 19:17", reply_markup=await main_menu('uz'))
    await state.set_state('in_start')

@dp.messgae_handler(state='week', text="Juma")
async def juma_function(message: types.Message, state: FSMContext):
    await message.answer("Juma \n\n☀️ +31°...+15°, Ochiq havo \n\nHozir: ☀️ +14°, ⬅️ 8 m/s \n\nTong: ☀️ +22° \nKun: ☀️ +29° \nOqshom: 🌤 +28° \n\nNamlik: 44% \nShamol: Shimoliy-shimoli-sharqiy, 7 m/s \nBosim: 762 mm sim. ust. \n\nOy: Yosh oy \nQuyosh chiqishi: 05:06 \nQuyosh botishi: 19:11", reply_markup=await main_menu('uz'))
    await state.set_state('in_start')

@dp.messgae_handler(state='week', text="Shanba")
async def shanba_function(message: types.Message, state: FSMContext):
    await message.answer("Shanba \n\n☀️ +36°...+20°, Ochiq havo \n\nYog'ingarchilik ehtimoli: 2%", reply_markup=await main_menu('uz'))
    await state.set_state('in_start')

@dp.messgae_handler(state='week', text="Yakshanba")
async def yakshanba_function(message: types.Message, state: FSMContext):
    await message.answer("Yakshanba \n\n☀️ +36°...+21°, Ochiq havo \n\nYog'ingarchilik ehtimoli: 1%", reply_markup=await main_menu('uz'))
    await state.set_state('in_start')
