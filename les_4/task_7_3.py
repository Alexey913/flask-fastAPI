#  Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
#  Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
#  Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
#  При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
#  В каждом решении нужно вывести время выполнения
# вычислений.


import multiprocessing as mp
import time
from random import randint as rnd


_LOW_LIMIT = 1
_HIGH_LIMIT = 100
_COUNT_ELEM = 1_000_000
_STEP = 200_000


def summ_numbers(q, arr, limit_1, limit_2):
    summ = 0
    for i in range(limit_1, limit_2):
        summ += arr[i]
    print(f"Подсчет суммы массива с {limit_1+1} по {limit_2+1} элементы \
за {time.time()-start_time:.2f} секунд")
    q.put(summ)


arr = [rnd(_LOW_LIMIT, _HIGH_LIMIT) for _ in range(1, _COUNT_ELEM+1)]
limit_1 = 0
limit_2 = limit_1 + _STEP

processes = []
start_time = time.time()

if __name__ == "__main__":
    mp.set_start_method('spawn')
    q = mp.Queue()
    res = 0
    while limit_2 <= _COUNT_ELEM:
        process = mp.Process(target=summ_numbers, args=(q, arr, limit_1, limit_2))
        process.start()
        limit_1, limit_2 = limit_2, limit_2 + _STEP
        res += q.get()
    
    for process in processes:
        process.join()

    print(f"Подсчет суммы методом разделения процессов: {res}")
    print(f"Итоговое время - {time.time()-start_time:.2f} секунд")