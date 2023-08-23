# Разработать API для управления списком пользователей с
# использованием базы данных SQLite. Для этого создайте
# модель User со следующими полями:
# ○ id: int (идентификатор пользователя, генерируется
# автоматически)
# ○ username: str (имя пользователя)
# ○ email: str (электронная почта пользователя)
# ○ password: str (пароль пользователя)

import databases
import sqlalchemy
from settings import settings

db = databases.Database(settings.DATABASE_URL)

metadata = sqlalchemy.MetaData()

...

users = sqlalchemy.Table('users', metadata,
                         sqlalchemy.Column('id',sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('username',sqlalchemy.String(32)),
                         sqlalchemy.Column('email',sqlalchemy.String(128)),
                         sqlalchemy.Column('password',sqlalchemy.String(128)),
                         )

posts = sqlalchemy.Table('posts', metadata,
                         sqlalchemy.Column('id',sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
                         sqlalchemy.Column('post',sqlalchemy.String(1024)),
                         )

engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)