from typing import List

from sqlalchemy import select
from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from db import db, users, posts
from random import randint as rnd

route = APIRouter()


# Добавление тестовых статей
@route.get("/fake_posts/{count}")
async def create_post(count: int):
    for i in range(count):
        query = posts.insert().values(post=f'{i*50*"post"}',
                                      user_id=rnd(1, 10))
        await db.execute(query)
    return {'message': f'{count} fake posts create'}

# Добавление статьи


@route.get("/posts/", response_model=list[Post])
async def get_post():
    query = select(
        posts.c.id, posts.c.post,
        users.c.id.label("user_id"),
        users.c.username, users.c.email,
        users.c.password
    ).join(users)
    rows = await db.fetch_all(query)
    return [Post(id=row.id,
                 post=row.post,
                 user=User(id=row.user_id,
                           username=row.username,
                           email=row.email,
                           password=row.password #Пароль никогда не выврдим, для вывода создаем отдельный класс без пароля
                           )) for row in rows]


# Создание статьи
@route.post("/posts/", response_model=dict)
async def create_post(post: PostIn):
    query = posts.insert().values(user_id=post.user_id,
                                  post=post.post)
    last_record_id = await db.execute(query)
    return {**post.model_dump(), "id": last_record_id}
