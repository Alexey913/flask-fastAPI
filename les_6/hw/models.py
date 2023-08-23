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

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    username: str = Field(title='Имя пользователя',
                          min_length=2, max_length=32)
    usersurname: str = Field(
        title='Фамилия пользователя', min_length=2, max_length=32)
    email: str = Field(title='E-mail')
    password: str = Field(title="Пароль", min_length=6)


class User(BaseModel):
    id: int = Field(title="id")
    username: str = Field(title='Имя пользователя',
                          min_length=2, max_length=32)
    usersurname: Optional[str] = Field(
        title='Фамилия пользователя', default=None, max_length=32)
    email: str = Field(title='E-mail')
    password: str = Field(title="Пароль", min_length=6)




class GoodsIn(BaseModel):
    title: str = Field(title='Наименование товара',
                       min_length=2, max_length=32)
    description: Optional[str] = Field(
        title='Описание товара', default=None, max_length=512)
    price: float = Field(title='Цена')


class Goods(BaseModel):
    id: int = Field(title="id")
    title: str = Field(title='Наименование товара',
                       min_length=2, max_length=32)
    description: Optional[str] = Field(
        title='Описание товара', default=None, max_length=512)
    price: float = Field(title='Цена', gt=0)




class OrderIn(BaseModel):
    user_id: int
    goods_id: int
    date: datetime = Field(title='Статус заказа', default=datetime.now())
    status: str = Field(title='Статус заказа', max_length=8)


class Order(BaseModel):
    id: int = Field(title="id")
    user: User
    goods: Goods
    date: datetime = Field(title='Статус заказа', default=datetime.now())
    status: str = Field(title='Статус заказа', max_length=8)