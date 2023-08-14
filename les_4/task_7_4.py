#  Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
#  Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
#  Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
#  При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
#  В каждом решении нужно вывести время выполнения
# вычислений.


import asyncio
import time
from random import randint as rnd


_LOW_LIMIT = 1
_HIGH_LIMIT = 100
_COUNT_ELEM = 1_000_000
_STEP = 200_000


async def summ_numbers(arr, limit_1, limit_2):
    global summ
    for i in range(limit_1, limit_2):
        summ += arr[i]
    print(f"Подсчет суммы массива с {limit_1+1} по {limit_2+1} элементы \
за {time.time()-start_time:.2f} секунд")
    return summ





async def main():
    arr = [rnd(_LOW_LIMIT, _HIGH_LIMIT) for _ in range(1, _COUNT_ELEM+1)]
    limit_1 = 0
    limit_2 = limit_1 + _STEP
    tasks = []
    while limit_2 <= _COUNT_ELEM:
        task = asyncio.create_task(summ_numbers(arr, limit_1, limit_2))
        tasks.append(task)
        limit_1, limit_2 = limit_2, limit_2 + _STEP
    await asyncio.gather(*tasks)

summ = 0
start_time = time.time()


if __name__ == "__main__":
    asyncio.run(main())
    print(f"Подсчет суммы методом асинхронного программирования: {summ}")
    print(f"Итоговое время - {time.time()-start_time:.2f} секунд")