# Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление


from typing import List
from models import Goods, GoodsIn
from fastapi import APIRouter
from db import db, goodses
from random import randint as rnd

route = APIRouter()


# Добавление тестовых товаров
@route.get("/fake_goods/{count}", summary='Создание тестовых товаров')
async def create_note(count: int):
    for i in range(count):
        query = goodses.insert().values(title=f'goods{i}',
                                      description=f'{"Описание " * rnd(int(i/2), i*2)}',
                                      price=float(rnd(1_000,100_000))
                                      )
        await db.execute(query)
    return {'message': f'{count} fake goodses create'}


# Создание товара
@route.post("/goodses/", response_model=Goods, summary='Создание товара')
async def create_goods(goods: GoodsIn):
    query = goodses.insert().values(title=goods.title,
                                  description=goods.description,
                                  price=goods.price)
    last_record_id = await db.execute(query)
    return {**goods.model_dump(), "id": last_record_id}


# Вывод всех товаров
@route.get("/goodses/", response_model=List[Goods], summary='Вывод списка товаров')
async def read_goodses():
    query = goodses.select()
    return await db.fetch_all(query)


# Вывод конкретного товара
@route.get("/goodses/{goods_id}", response_model=Goods, summary='Поиск товара по id')
async def read_goods(goods_id: int):
    query = goodses.select().where(goodses.c.id == goods_id)
    return await db.fetch_one(query)


# Обновление товара
@route.put("/goodses/{goods_id}", response_model=Goods, summary='Обновление товара по id')
async def update_goods(goods_id: int, new_goods: GoodsIn):
    query = goodses.update().where(goodses.c.id == goods_id).values(**new_goods.model_dump())
    await db.execute(query)
    return {**new_goods.model_dump(), "id": goods_id}


# Удаление товара
@route.delete("/goodses/{goods_id}", summary='Удаление товара по id')
async def delete_goods(goods_id: int):
    query = goodses.delete().where(goodses.c.id == goods_id)
    await db.execute(query)
    return {'message': 'goods deleted'}