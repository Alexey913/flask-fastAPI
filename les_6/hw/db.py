# Необходимо создать базу данных для интернет-магазина. База данных должна
# состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
# содержать информацию о доступных товарах, их описаниях и ценах. Таблица
# пользователи должна содержать информацию о зарегистрированных
# пользователях магазина. Таблица заказы должна содержать информацию о
# заказах, сделанных пользователями.
# ○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
# имя, фамилия, адрес электронной почты и пароль.
# ○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
# название, описание и цена.
# ○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
# пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
# заказа.

# Создайте модели pydantic для получения новых данных и
# возврата существующих в БД для каждой из трёх таблиц
# (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление

import databases
import sqlalchemy
from settings import settings

db = databases.Database(settings.DATABASE_URL)

metadata = sqlalchemy.MetaData()

...

users = sqlalchemy.Table('users', metadata,
                         sqlalchemy.Column('id',sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('username',sqlalchemy.String(32), nullable=False),
                         sqlalchemy.Column('usersurname',sqlalchemy.String(32)),
                         sqlalchemy.Column('email',sqlalchemy.String(128), nullable=False),
                         sqlalchemy.Column('password',sqlalchemy.String(128), nullable=False),
                         )

goodses = sqlalchemy.Table('goods', metadata,
                         sqlalchemy.Column('id',sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('title',sqlalchemy.String(32), nullable=False),
                         sqlalchemy.Column('description',sqlalchemy.String(512)),
                         sqlalchemy.Column('price',sqlalchemy.Float, nullable=False),
                         )

orders = sqlalchemy.Table('orders', metadata,
                         sqlalchemy.Column('id',sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
                         sqlalchemy.Column('goods_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('goods.id'), nullable=False),
                         sqlalchemy.Column('date', sqlalchemy.DateTime, nullable=False),
                         sqlalchemy.Column('status', sqlalchemy.String(8), nullable=False),
                         )

engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)