from aiogram import Bot, Dispatcher, types, filters, F
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

# import requests

bot = Bot(token='7364081736:AAFGFjg42OdyOUWKwx6fVynCSSVxBbEURbI')
dp = Dispatcher(bot=bot)


class Card(StatesGroup):
    card_number = State()
    card_number_2 = State()


class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()


contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)

button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🌤 Ob-Havo"), KeyboardButton(text="☘️ Sog'lom turmush tarzi")],
    [KeyboardButton(text="🚑 Xizmatlar"), KeyboardButton(text="🏆 Marafon")],
    [KeyboardButton(text="🛒 Savat")]
], resize_keyboard=True)

savat_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="💸 Sotib olish"), KeyboardButton(text="🚮 Savatni tozalash")],
    [KeyboardButton(text="🗑 Savatni ko'rish"), KeyboardButton(text="🔙 Orqaga")]
], resize_keyboard=True)

hafta = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Dushanba"), KeyboardButton(text="Seshanba")],
    [KeyboardButton(text="Chorshanba"), KeyboardButton(text="Payshanba")],
    [KeyboardButton(text="Juma"), KeyboardButton(text="Shanba")],
    [KeyboardButton(text="Yakshanba"), KeyboardButton(text="🔙 orqaga")]
], resize_keyboard=True)

soglom = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌐 Batafsil ma'lumot", url="https://uz.wikipedia.org/wiki/Sog%CA%BBlom_turmush_tarzi")],
    [InlineKeyboardButton(text="🎥 Video darslik", url="https://www.youtube.com/watch?v=fR1tlp8odU8")],
    [InlineKeyboardButton(text="🧑‍🏫 Darslarga yozilish", callback_data="muddat")],
    [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="ortga")]
])

muddat = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌘 3 oy", callback_data="3"), InlineKeyboardButton(text="🌗 6 oy", callback_data="6")],
    [InlineKeyboardButton(text="🌑 12 oy", callback_data="12"), InlineKeyboardButton(text="🌓 18 oy", callback_data="18")]
])

pay_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ O'qishni boshlash", callback_data="oqish_3")],
    [InlineKeyboardButton(text="❌ O'qishni tugatish", callback_data="orqaga")]
])

pay_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ O'qishni boshlash", callback_data="oqish_6")],
    [InlineKeyboardButton(text="❌ O'qishni tugatish", callback_data="orqaga")]
])

pay_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ O'qishni boshlash", callback_data="oqish_12")],
    [InlineKeyboardButton(text="❌ O'qishni tugatish", callback_data="orqaga")]
])

pay_18 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ O'qishni boshlash", callback_data="oqish_18")],
    [InlineKeyboardButton(text="❌ O'qishni tugatish", callback_data="orqaga")]
])

police = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌐 Batafsil ma'lumot", url="https://www.gazeta.uz/oz/2019/07/21/order/")],
    [InlineKeyboardButton(text="🎥 Video darslik", url="https://www.youtube.com/watch?v=xIMdg1DKQpw")],
    [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="ortga")]
])

ochirish = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌐 Batafsil ma'lumot", url="https://www.gazeta.uz/oz/2021/11/29/fire-extinguisher/")],
    [InlineKeyboardButton(text="🎥 Video darslik", url="https://www.youtube.com/watch?v=3BYJkcWPnIM")],
    [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="ortga")]
])

pomosh = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌐 Batafsil ma'lumot", url="https://uz.wikipedia.org/wiki/103")],
    [InlineKeyboardButton(text="🎥 Video darslik", url="https://www.youtube.com/watch?v=4gU6Ys_e33c")],
    [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="ortga")]
])

marafon = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🏃 Yugurish"), KeyboardButton(text="🏊‍♂️ Suzish")],
    [KeyboardButton(text="🚴 Velo poyga"), KeyboardButton(text="⚽️ Futbol")],
    [KeyboardButton(text="🏐 Volleybol"), KeyboardButton(text="🎾 Tennis")],
    [KeyboardButton(text="🔙 orqaga")]
], resize_keyboard=True)

viloyat = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Toshkent"), KeyboardButton(text="Andijon")],
    [KeyboardButton(text="Farg'ona"), KeyboardButton(text="Guliston")],
    [KeyboardButton(text="Jizzax"), KeyboardButton(text="Buxoro")]
], resize_keyboard=True)

xizmatlar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🚒 101"), KeyboardButton(text="🚓 102")],
    [KeyboardButton(text="🚑 103"), KeyboardButton(text="🔙 orqaga")]
], resize_keyboard=True)

cart = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳 Uzcard", callback_data="Uzcard")],
    [InlineKeyboardButton(text="💳 Humo", callback_data="Humo")],
])

orders =[]

@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer("Botga xush kelibsiz !!!", reply_markup=button)


@dp.message(F.text == "🔙 orqaga")
async def orqaga_function(message: types.Message):
    await message.answer("Siz orqaga qaytdingiz", reply_markup=button)


@dp.callback_query(F.data == "ortga")
async def ortga_function(call: types.CallbackQuery):
    await call.message.answer("Siz orqaga qaytdingiz", reply_markup=button)


@dp.message(F.text == "🌤 Ob-Havo")
async def obhavo_function(message: types.Message):
    await message.answer_photo(photo="https://obhavo.uz/images/preview-logo-uz.png",
                               caption="Siz qaysi kunning ob havosini bilmoqchisiz",
                               reply_markup=hafta)


@dp.message(F.text == "🚑 Xizmatlar")
async def obhavo_function(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7IsQ0i6ZI5jTkUybFRsG_k96LEwmbgc2sWg&s",
        caption="Siz qaysi xizmatdan foydalanmoqchisiz ?",
        reply_markup=xizmatlar)


@dp.message(F.text == "🚑 103")
async def obhavo_function(message: types.Message):
    await message.answer("103 xizmati", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://storage.kun.uz/source/9/aihXC6HVXcfChwMItsl0lxQnuvGO3AZW.jpg",
        caption="Siz 103 xizmatidan foydalanyapsiz \n\n2020 yilda «103» tez tibbiy yordam raqamiga 10 milliondan oshiq murojaatlar kelib tushgan. Shundan 800 mingdan ortig‘i Toshkent shahri hissasiga to‘g‘ri kelmoqda. Bu haqda Sog‘liqni saqlash vaziri o‘rinbosari Abdulla Azizov yangi 103 avtomatlashtirilgan boshqaruv tizimida faol ishlagan tez tibbiy yordam podstansiyalarini taqdirlash marosimida ma'lum qildi. \n\nTez tibbiy yordam tizimi faoliyatini samarali yo‘lga qo‘yish maqsadida Sog‘liqni saqlash vazirligi, Respublika shoshilinch tibbiy yordam ilmiy markazi va «BePro» dasturchilar markazi o‘zaro hamkorlik loyihasiga qo‘l urgan.",
        reply_markup=pomosh)

@dp.message(F.text == "🚓 102")
async def obhavo_function(message: types.Message):
    await message.answer("102 xizmati", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyAsNHn5RXJf3ZWo2iuPg5MV-inV5ChkfuHA&s",
        caption="Siz 102 xizmatidan foydalanyapsiz \n\nXodimlar huquqbuzarlikni bartaraf etishlarini kutib turibman. Jarima yozishadi. Musiqa to‘xtaydi. Biroq buning o‘rniga meni haqorat qilayotgan klub xodimlari ko‘z oldida Abduraxmonov kuch ishlatib mening telefonimini olib ko‘ydi va cho‘ntagiga soldi. Sattorov esa mashinaga o‘tirib, uchastkaga borishga buyuradi. Uchastkaga kelgandan so‘ng u choralar ko‘rilgani haqidagi qog‘ozga qo‘l qo‘yishimni talab qiladi. Haqoratli so‘zlar bilan so‘kinadi. Eshiklarni qattiq yopadi. Astoydil talablardan so‘ng qo‘yib yuboradi va uchastkadan noma’lum tarafga jo‘nab ketadi. \n\n102 yana to‘rt ko‘ng‘iroq. Endi hech kim kelmaydi. 04:30. Diskoteka davom etadi.",
        reply_markup=police)


@dp.message(F.text == "🚒 101")
async def obhavo_function(message: types.Message):
    await message.answer("101 xizmati", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_95FKKzw1u5ycx6c-TLy6Z3crWtUlJCiAnA&s",
        caption="Siz 101 xizmatidan foydalanyapsiz. \n\nSovuq fasllar kirib kelishi bilan binolarda yong‘in xavfi ortadi. Yong‘inga qarshi kurashning eng samarali vositasi o‘t o‘chirgich hisoblanadi. Ularni ko‘pincha ofislarda va mashinalarda uchratish mumkin, ammo hamma ham ulardan qanday foydalanish to‘g‘risida ma’lumotga ega emas. O‘t o‘chirgichning turlari va ulardan to‘g‘ri foydalanish qoidalari haqida o‘t o‘chiruvchi Aleksey Sorochin «Gazeta.uz»ga so‘zlab berdi. \n\nYong‘inlar o‘z-o‘zidan paydo bo‘lmaydi, lekin har qanday yong‘inning ham oldini olish mumkin. Yong‘inga qarshi birlamchi kurashish vositasi o‘t o‘chirgichlar hisoblanadi. Ular barcha xonalarda va transport vositalarida o‘rnatilishi kerak. O‘t o‘chirgichlarning turli xil bo‘lishini esa hamma ham bilmaydi. Bundan tashqari, hammada ham ulardan qanday foydalanish to‘g‘risida ma’lumot mavjud emas.",
        reply_markup=ochirish)


@dp.message(F.text == "☘️ Sog'lom turmush tarzi")
async def soglom_function(message: types.Message):
    await message.answer("☘️ Sog'lom turmush tarzi", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://www.forumdaily.com/wp-content/uploads/2018/09/Depositphotos_160465120_m-2015.jpg",
        caption="Sogʻlom turmush tarzi ( STT ) – bu xatti-harakatlarning xavf omillarini nazorat qilish orqali sog'lig'ini saqlashga va yuqumli bo'lmagan kasalliklar (NCD) xavfini kamaytirishga yordam beradigan insonning turmush tarzidir [1] . \n\nSogʻlom turmush tarzi tamaki va spirtli ichimliklarni iste'mol qilishdan voz kechish, muvozanatli ovqatlanish, jismoniy faollik ( jismoniy mashqlar, sport va boshqalar), ruhiy salomatlikni mustahkamlash va boshqa sog'liqni saqlash choralarini oʻz ichiga oladi [1] \n\nSoʻgʻlom turmush tarzi tamoyillari odatda erta yoshda belgilanadi. Sogʻlom turmush tarzini ushbu yoshda shakllantirish muhimdir, chunki yoshlarda shakllangan odatlar ko'pincha balog'at yoshiga qadar saqlanib qoladi [2] .",
        reply_markup=soglom)

@dp.callback_query(F.data == "muddat")
async def muddat_function(call: types.CallbackQuery):
    await call.message.answer("Siz kunlik darslar bo'limiga o'tdingiz !", reply_markup=muddat)

@dp.callback_query(F.data == "3")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://uzpharmagency.uz/uploads/news/dfe559dde2514e58b104e10408755cbf.jpg",
        caption="Siz 3 oyli o'qish turini tanladingiz.", reply_markup=pay_3)


@dp.callback_query(F.data == "oqish_3")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 3 oyli o'qish")
    await call.message.answer(
        "Siz 3 oyli o'qishni tanladingiz. \nTo'lovni savat bo'limidan amalga oshirishingiz mumkin",
        reply_markup=button)


@dp.callback_query(F.data == "6")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://uzpharmagency.uz/uploads/news/dfe559dde2514e58b104e10408755cbf.jpg",
        caption="Siz 6 oyli o'qish turini tanladingiz.", reply_markup=pay_6)


@dp.callback_query(F.data == "oqish_6")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 6 oyli o'qish")
    await call.message.answer(
        "Siz 6 oyli o'qishni tanladingiz. \nTo'lovni savat bo'limidan amalga oshirishingiz mumkin",
        reply_markup=button)


@dp.callback_query(F.data == "12")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://uzpharmagency.uz/uploads/news/dfe559dde2514e58b104e10408755cbf.jpg",
        caption="Siz 12 oyli o'qish turini tanladingiz.", reply_markup=pay_12)


@dp.callback_query(F.data == "oqish_12")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 12 oyli o'qish")
    await call.message.answer(
        "Siz 12 oyli o'qishni tanladingiz. \nTo'lovni savat bo'limidan amalga oshirishingiz mumkin",
        reply_markup=button)


@dp.callback_query(F.data == "18")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://uzpharmagency.uz/uploads/news/dfe559dde2514e58b104e10408755cbf.jpg",
        caption="Siz 18 oyli o'qish turini tanladingiz.", reply_markup=pay_18)


@dp.callback_query(F.data == "oqish_18")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 18 oyli o'qish")
    await call.message.answer(
        "Siz 18 oyli o'qishni tanladingiz. \nTo'lovni savat bo'limidan amalga oshirishingiz mumkin",
        reply_markup=button)



@dp.message(F.text == "🏆 Marafon")
async def marafon_function(message: types.Message):
    await message.answer_photo(
        photo="https://as2.ftcdn.net/v2/jpg/02/68/51/69/1000_F_268516931_XKoOPpfwrXTrMmfsQBGiKDbJhFvjgUD4.jpg",
        caption="Marafonga xush kelibsiz \nO'zizga yoqqan sport turini tanlang ?", reply_markup=marafon)


@dp.message(F.text == "🏃 Yugurish")
async def marafon_function(message: types.Message):
    await message.answer_photo(
        photo="https://img.freepik.com/free-vector/marathon-race_52683-10874.jpg?size=626&ext=jpg&ga=GA1.1.2008272138.1721001600&semt=ais_user",
        caption="Siz yugurish marafonini tanladingiz \nQaysi viloyatda qatnashmoqchisiz ?", reply_markup=viloyat)


@dp.message(F.text == "🏊‍♂️ Suzish")
async def marafon_function(message: types.Message):
    await message.answer_photo(photo="https://kuda-spb.ru/uploads/21065a681432e1a73d7bcaa4e3c6f8b1.png",
                               caption="Siz suzish marafonini tanladingiz \nQaysi viloyatda qatnashmoqchisiz ?",
                               reply_markup=viloyat)


@dp.message(F.text == "🚴 Velo poyga")
async def marafon_function(message: types.Message):
    await message.answer_photo(photo="https://daryo.uz/static/2024/07/10/2--z3Q-yGI.jpg",
                               caption="Siz velo poyga marafonini tanladingiz \nQaysi viloyatda qatnashmoqchisiz ?",
                               reply_markup=viloyat)


@dp.message(F.text == "⚽️ Futbol")
async def marafon_function(message: types.Message):
    await message.answer_photo(photo="https://daryo.uz/cache/2022/03/zdQkAcQV-954x522.jpg",
                               caption="Siz futbol marafonini tanladingiz \nQaysi viloyatda qatnashmoqchisiz ?",
                               reply_markup=viloyat)


@dp.message(F.text == "🏐 Volleybol")
async def marafon_function(message: types.Message):
    await message.answer_photo(
        photo="https://www.volleyball.ua/media/cache/post_pic/uploads/posts/16782758416408750129363.jpeg",
        caption="Siz volleybol marafonini tanladingiz \nQaysi viloyatda qatnashmoqchisiz ?", reply_markup=viloyat)


@dp.message(F.text == "🎾 Tennis")
async def marafon_function(message: types.Message):
    await message.answer_photo(photo="https://aniq.uz/photos/news/0c4dSf0Lg5wBGxo.jpeg",
                               caption="Siz tennis marafonini tanladingiz \nQaysi viloyatda qatnashmoqchisiz ?",
                               reply_markup=viloyat)

@dp.message(F.text == "💸 Sotib olish")
async def savat_function(message: types.Message):
    await message.answer("To'lov turini tanlang Uzcard yoki Humo orqali to'lash", reply_markup=cart)


@dp.message(F.text == "🛒 Savat")
async def savat_function(message: types.Message):
    await message.answer("Siz savat bo'limini tanladingiz !", reply_markup=savat_button)


@dp.message(F.text == "🗑 Savatni ko'rish")
async def orders_function(message: types.Message):
    await message.answer(f"Sizda bor kurslar ro'yxati !!!")
    await message.answer(f"{"\n".join(orders)}", reply_markup=button)


@dp.message(F.text == "🚮 Savatni tozalash")
async def ordersdell_function(message: types.Message):
    orders.clear()
    await message.answer("Siz barcha kurslarni o'chirib yubordingiz !!!", reply_markup=button)

@dp.message(F.text == "Dushanba")
async def dushanba_function(message: types.Message):
    await message.answer("Dushanba \n\n☀️ +38°...+20°, Ochiq havo \n\nHozir: ☀️ +25°, ⬅️ 10 m/s \n\nTong: ☀️ +29° \nKun: ☀️ +36° \nOqshom: ☀️ +35° \n\nNamlik: 40% \nShamol: Sharqiy-shimoli-sharq, 9 m/s \nBosim: 758 mm sim. ust. \n\nOy: Yosh oy \nQuyosh chiqishi: 04:42 \nQuyosh botishi: 19:39", reply_markup=button)


@dp.message(F.text == "Seshanba")
async def seshanba_function(message: types.Message):
    await message.answer("Seshanba \n\n☀️ +25°...+13°, Ochiq havo \n\nYog'ingarchilik ehtimoli: 6%", reply_markup=button)

@dp.message(F.text == "Chorshanba")
async def chorshanba_function(message: types.Message):
    await message.answer("Seshanba \n\n☀️ +25°...+13°, Ochiq havo \n\nYog'ingarchilik ehtimoli: 6%", reply_markup=button)

@dp.message(F.text == "Payshanba")
async def payshanba_function(message: types.Message):
    await message.answer("Chorshanba \n\n🌧 +28°...+13°, Yomg'ir \n\nHozir: 🌤 +16°, ↙️ 8 m/s \n\nTong: ☀️ +21° \nKun: ☀️ +27° \nOqshom: ☀️ +26° \n\nNamlik: 54% \nShamol: Shimoliy-shimoli-sharqiy, 7 m/s \nBosim: 767 mm sim. ust. \n\nOy: Qisqarayotgan oy \nQuyosh chiqishi: 04:59 \nQuyosh botishi: 19:17", reply_markup=button)

@dp.message(F.text == "Juma")
async def juma_function(message: types.Message):
    await message.answer("Juma \n\n☀️ +31°...+15°, Ochiq havo \n\nHozir: ☀️ +14°, ⬅️ 8 m/s \n\nTong: ☀️ +22° \nKun: ☀️ +29° \nOqshom: 🌤 +28° \n\nNamlik: 44% \nShamol: Shimoliy-shimoli-sharqiy, 7 m/s \nBosim: 762 mm sim. ust. \n\nOy: Yosh oy \nQuyosh chiqishi: 05:06 \nQuyosh botishi: 19:11", reply_markup=button)

@dp.message(F.text == "Shanba")
async def shanba_function(message: types.Message):
    await message.answer("Shanba \n\n☀️ +36°...+20°, Ochiq havo \n\nYog'ingarchilik ehtimoli: 2%", reply_markup=button)

@dp.message(F.text == "Yakshanba")
async def yakshanba_function(message: types.Message):
    await message.answer("Yakshanba \n\n☀️ +36°...+21°, Ochiq havo \n\nYog'ingarchilik ehtimoli: 1%", reply_markup=button)

@dp.message(F.text == "Toshkent")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Registratsiyadan o'tib oling !\nIsmingizni kiriting: ", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "Andijon")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Registratsiyadan o'tib oling !\nIsmingizni kiriting: ", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "Farg'ona")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Registratsiyadan o'tib oling !\nIsmingizni kiriting: ", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "Guliston")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Registratsiyadan o'tib oling !\nIsmingizni kiriting: ", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "Jizzax")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Registratsiyadan o'tib oling !\nIsmingizni kiriting: ", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "Buxoro")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Registratsiyadan o'tib oling !\nIsmingizni kiriting: ", reply_markup=ReplyKeyboardRemove())


@dp.message(Registration.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Yaxshi endi familya kiriting: ", reply_markup=ReplyKeyboardRemove())


@dp.message(Registration.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.number)
    await message.answer("Yaxshi endi raqamingizni kiriting: ", reply_markup=contact_button)


@dp.message(Registration.number)
async def phone_function(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f"Gap yo'q!\nSizning ismingiz: {data['first_name']}\nSizning familyangiz: {data['last_name']}\nSizning nomeringiz: {data['number']} \n\nTabriklaymiz !!! siz marafonga yozildingiz",
        reply_markup=button)
    await state.clear()


@dp.callback_query(F.data == "Uzcard")
async def pey_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.card_number)
    await call.message.answer("Karta raqamini kiriting: ")


@dp.message(Card.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        orders.clear()
        await state.update_data(card_number=message.text)
        await message.answer(
            f"\n \n Rahmat {message.from_user.full_name} siz to'lovni Uzcard kartasi orqali omalga oshirdingiz. \nBizdan harid qilganingiz uchun rahmat!!! \nYana harid qilmoqchi bo'lsangiz menu bo'limiga o'ting.",
            reply_markup=button)
    else:
        await message.answer("Boshidan urinib ko'ring !!!", reply_markup=cart)
    await state.clear()


@dp.callback_query(F.data == "Humo")
async def pay_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.card_number_2)
    await call.message.answer("Karta raqamini kiriting: ")


@dp.message(Card.card_number_2)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        orders.clear()
        await state.update_data(card_number=message.text)
        await message.answer(
            f"\n \n Rahmat {message.from_user.full_name} siz Humo kartasi orqali to'lovni omalga oshirdingiz. \nBizdan harid qilganingiz uchun rahmat!!! \nYana harid qilmoqchi bo'lsangiz menu bo'limiga o'ting.",
            reply_markup=button)
    else:
        await message.answer("Boshidan urinib ko'ring !!!", reply_markup=cart)
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
