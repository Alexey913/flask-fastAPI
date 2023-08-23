# API должно поддерживать следующие операции:
# ○ Получение списка всех пользователей: GET /users/
# ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
# ○ Создание нового пользователя: POST /users/
# ○ Обновление информации о пользователе: PUT /users/{user_id}/
# ○ Удаление пользователя: DELETE /users/{user_id}/

# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.


from typing import List
from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from db import db, users
from random import randint as rnd

route = APIRouter()


# Добавление тестовых пользователей
@route.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(username=f'user{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=rnd(100000, 999999))
        await db.execute(query)
    return {'message': f'{count} fake users create'}


# Создание пользователя
@route.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username,
                                  email=user.email,
                                  password=user.password)
    last_record_id = await db.execute(query)
    return {**user.model_dump(), "id": last_record_id}


# Вывод всех пользователей
@route.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await db.fetch_all(query)


# Вывод конкретного пользователя
@route.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await db.fetch_one(query)


# Обновление пользователя
@route.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await db.execute(query)
    return {**new_user.model_dump(), "id": user_id}

# Удаление пользователя
@route.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await db.execute(query)
    return {'message': 'User deleted'}