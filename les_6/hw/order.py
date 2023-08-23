# Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление


from typing import List

from sqlalchemy import select, join
from models import Order, OrderIn, User, Goods
from fastapi import APIRouter
from db import db, users, goodses, orders
from random import randint as rnd
from datetime import datetime

route = APIRouter()


# Создание заказа
@route.post("/orders/", response_model=dict, summary='Создание заказа')
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id,
                                   goods_id=order.goods_id,
                                   date=datetime.now(),
                                   status=order.status)
    last_record_id = await db.execute(query)
    return {**order.model_dump(), "id": last_record_id}



# Вывод всех заказов
@route.get("/orders/", response_model=list[Order], summary='Вывод списка заказов')
async def get_orders():
    query = select(
             orders.c.id, orders.c.status, orders.c.date,
             users.c.id.label("user_id"),
             users.c.username, users.c.usersurname,
             users.c.email, users.c.password,
             goodses.c.id.label("goods_id"),
             goodses.c.title, goodses.c.description, goodses.c.price,
                   ).join(users).join(goodses)
    rows = await db.fetch_all(query)
    return [Order(id=row.id,
                  user=User(id=row.user_id,
                            username=row.username,
                            usersurname=row.usersurname,
                            email=row.email,
                            password=row.password
                            ),
                  goods=Goods(id=row.goods_id,
                              title=row.title,
                              description=row.description,
                              price=row.price
                              ),
                  date=row.date,
                  status=row.status
                  ) 
                  for row in rows]

# Вывод конкретного заказа
@route.get("/orders/{order_id}", response_model=Order, summary='Поиск заказа по id')
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await db.fetch_one(query)


# Обновление заказа
@route.put("/orders/{order_id}", response_model=dict, summary='Обновление заказа по id')
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(
        orders.c.id == order_id).values(**new_order.model_dump())
    await db.execute(query)
    return {"id": order_id, **new_order.model_dump()}


# Удаление заказа
@route.delete("/orders/{order_id}", summary='Удаление заказа по id')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await db.execute(query)
    return {'message': 'Order deleted'}
