# Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление


from typing import List
from models import User, UserIn
from fastapi import APIRouter
from db import db, users
from random import randint as rnd

route = APIRouter()


# Добавление тестовых пользователей
@route.get("/fake_users/{count}", summary='Добавление тестовых пользователей')
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(username=f'user{i}',
                                      usersurname=f'surname{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=rnd(100000, 999999))
        await db.execute(query)
    return {'message': f'{count} fake users create'}


# Создание пользователя
@route.post("/users/", response_model=User, summary='Создание пользователя')
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username,
                                  usersurname=user.usersurname,
                                  email=user.email,
                                  password=user.password)
    last_record_id = await db.execute(query)
    return {**user.model_dump(), "id": last_record_id}


# Вывод всех пользователей
@route.get("/users/", response_model=List[User], summary='Вывод списка пользователей')
async def read_users():
    query = users.select()
    return await db.fetch_all(query)


# Вывод конкретного пользователя
@route.get("/users/{user_id}", response_model=User, summary='Поиск пользователя по id')
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await db.fetch_one(query)


# Обновление пользователя
@route.put("/users/{user_id}", response_model=User, summary='Обновление пользователя по id')
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await db.execute(query)
    return {**new_user.model_dump(), "id": user_id}


# Удаление пользователя
@route.delete("/users/{user_id}", summary='Удаление пользователя по id')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await db.execute(query)
    return {'message': 'User deleted'}