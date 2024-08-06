from .database_settings import metadata
from sqlalchemy import Table, String, Integer, Boolean, Column, BigInteger, Text

users = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('full_name', String, nullable=True),
    Column('chat_id', BigInteger, nullable=False),
    Column('lang', String, nullable=False),
    Column('phone_number', String, nullable=False)
)

problems = Table(
    "problems",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(50), nullable=False),
    Column('description', Text, nullable=False),
    Column('photo', String, nullable=True),
    Column('chat_id', BigInteger, nullable=False)
)

works = Table(
    'works',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('description', String, nullable=False),
    Column('complete', Boolean, default=False),
    Column('photo', String, nullable=False),
    Column('chat_id', BigInteger, nullable=False)
)

