#  Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
#  Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
#  Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
#  При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
#  В каждом решении нужно вывести время выполнения
# вычислений.


import threading
import time
from random import randint as rnd


_LOW_LIMIT = 1
_HIGH_LIMIT = 100
_COUNT_ELEM = 1_000_000
_STEP = 200_000


def summ_numbers(arr, limit_1, limit_2):
    summ = 0
    for i in range(limit_1, limit_2):
        summ += arr[i]
    print(f"Подсчет суммы массива с {limit_1+1} по {limit_2+1} элементы \
за {time.time()-start_time:.2f} секунд")
    summ_list.append(summ)

arr = [rnd(_LOW_LIMIT, _HIGH_LIMIT) for _ in range(1, _COUNT_ELEM+1)]
limit_1 = 0
limit_2 = limit_1 + _STEP

threads = []
summ_list = []
start_time = time.time()

if __name__ == "__main__":
    while limit_2 <= _COUNT_ELEM:
        thread = threading.Thread(target=summ_numbers, args=[arr, limit_1, limit_2])
        threads.append(thread)
        thread.start()
        limit_1, limit_2 = limit_2, limit_2 + _STEP
    
    for thread in threads:
        thread.join()

    print(f"Подсчет суммы методом разделения потоков: {sum(summ_list)}")
    print(f"Итоговое время - {time.time()-start_time:.2f} секунд")
    