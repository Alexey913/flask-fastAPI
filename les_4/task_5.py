# Создать программу, которая будет производить подсчет 
# количества слов в каждом файле в указанной директории и 
# выводить результаты в консоль.
# Используйте процессы.

import requests
from multiprocessing import Process, Pool
import time
import os


def count_word(file, folder):
    count = 0
    filename = os.path.join(folder, file)
    if os.path.isfile(filename):
        with open(filename, "r", encoding='utf-8') as f:
            for line in f:
                count+=len(line.split())
        with open("./les_4/task_5.txt", "a", encoding='utf-8') as res:
            res.write(file + " - количество слов: " + str(count) + "\n")
            print(f"Подсчет слов в файле {file} за {time.time()-start_time:.2f} секунд")


processes = []
start_time = time.time()
folder = os.getcwd() + "\\les_2\\templates"

if __name__ == "__main__":
    files=os.listdir(folder)
    for file in files:
        process = Process(target=count_word, args=(file, folder))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()