from loader import  _
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def main_menu(lang):
    main_menu_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_(f"🎉 Tadbirlar", locale=lang))
            ],
            [
                KeyboardButton(text=_(f"❗️ Shikoyatlar", locale=lang)),
                KeyboardButton(text=_(f"👩‍🏫 Darsliklar", locale=lang))
            ],
            [
                KeyboardButton(text=_(f"🌤 Ob havo", locale=lang)),
                KeyboardButton(text=_(f"⚙️ Sozlamalar", lcoale=lang))
            ]
        ], resize_keyboard=True
    )
    return main_menu_btn

async def user_settings_menu(lang):
    settings = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_(f"👤 Ism Familyani O'zgartirish", locale=lang)),
                KeyboardButton(text=_(f"📞 Telefon Raqamni O'zgartirish", locale=lang)),
            ],
            [
                KeyboardButton(text=_(f"🇺🇿 🔁 🇷🇺 Tilni O'zgartirish", locale=lang)),
                KeyboardButton(text=_(f"🏘 Asosiy Menyu", locale=lang))
            ]
        ], resize_keyboard=True
    )
    return settings

async def weeks(lang):
    hafta = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Dushanba"),
                KeyboardButton(text="Seshanba")
            ],
            [
                KeyboardButton(text="Chorshanba"),
                KeyboardButton(text="Payshanba")
            ],
            [
                KeyboardButton(text="Juma"),
                KeyboardButton(text="Shanba")
            ],
            [
                KeyboardButton(text="Yakshanba"),
                KeyboardButton(text="🔙 orqaga")
            ]
    ], resize_keyboard=True
    )
    return hafta

async def lesson_courses(lang):
    lesson_courses_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_(f"🌘 3 Oy", locale=lang)),
                KeyboardButton(text=_(f"🌗 6 Oy", locale=lang)),
            ],
            [
                KeyboardButton(text=_(f"🌑 12 Oy", locale=lang)),
                KeyboardButton(text=_(f"🌓 18 Oy", locale=lang)),
            ]
        ], resize_keyboard=True
    )
    return lesson_courses_btn

async def problems(lang):
    problems_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_(f"‼️ Mening shikoyatlarim", locale=lang)),
                KeyboardButton(text=_(f"➕‼️ Shikoyat berish", locale=lang)),
            ],
            [
                KeyboardButton(text=_(f"❗️ Barcha Shikoyatlar", locale=lang)),
                KeyboardButton(text=_(f"🏘 Asosiy menyu", lcoale=lang))
            ]
        ], resize_keyboard=True
    )
    return problems_btn

async def events(lang):
    events_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_(f"🎉 Barcha tadbirlar", lcoale=lang)),
                KeyboardButton(text=_(f"➕🎉 Tadbir qoshish", locale=lang))
            ],
            [
                KeyboardButton(text=_(f"👤🎉 Mening tadbirlarim", locale=lang)),
                KeyboardButton(text=_(f"❌ Bekor qilish", locale=lang))
            ]
        ], resize_keyboard=True
    )
    return events_btn

async def cancel(lang):
    cancel_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_(f"❌ Bekor qilish", lcaole=lang))
            ]
        ], resize_keyboard=True
    )
