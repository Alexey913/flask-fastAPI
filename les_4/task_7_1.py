#  Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
#  Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
#  Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
#  При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
#  В каждом решении нужно вывести время выполнения
# вычислений.


import time
from random import randint as rnd


_LOW_LIMIT = 1
_HIGH_LIMIT = 100
_COUNT_ELEM = 1_000_000


def sum_numbers(arr, sum, limit_1, limit_2):
    for i in range(limit_1, limit_2):
        sum += arr[i]
    print(f"Подсчет суммы массива с {limit_1+1} по {limit_2+1} элементы \
за {time.time()-start_time:.2f} секунд")
    return sum


def sync_sum(arr):
    sum = 0
    for i in range(_COUNT_ELEM):
        sum += arr[i]
    print(f"Подсчет суммы массива синхронным методом за {time.time()-start_time:.2f} секунд")
    return sum


arr = [rnd(_LOW_LIMIT, _HIGH_LIMIT) for _ in range(1, _COUNT_ELEM+1)]

start_time = time.time()

if __name__ == "__main__":
    print(f"Подсчет суммы синхронным методом: {sync_sum(arr)}")
