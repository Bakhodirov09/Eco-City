from main.database_settings import database
from main.models import users, problems, works

async def get_user(chat_id):
    return await database.fetch_one(query=users.select().where(
        users.c.chat_id == chat_id
    ))

async def add_user(chat_id, full_name, phone_number, lang):
    if not await get_user(chat_id=chat_id):
        return await database.execute(query=users.insert().values(
            full_name=full_name,
            chat_id=chat_id,
            lang=lang,
            phone_number=phone_number
        ))

async def add_event(data):
    return await database.execute(query=works.insert().values(
        title=data['title'],
        description=data['desc'],
        photo=data['photo'],
        chat_id=data['chat_id']
    ))

async def add_problem(data):
    return await database.execute(query=problems.insert().values(
        title=data['title'],
        photo=data['photo'],
        chat_id=data['chat_id']
    ))

async def get_all_problems_user(chat_id):
    return await database.fetch_all(query=problems.select().where(
        users.c.chat_i == chat_id
    ))

async def get_all_problems():
    return await database.fetch_all(query=problems.select())