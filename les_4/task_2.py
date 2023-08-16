# аписать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса. 
#  После загрузки данных нужно записать их в отдельные файлы.
#  Используйте процессы.

import requests
from multiprocessing import Process, Pool
import time
import os


urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://www.ozon.ru/',
        'https://mail.ru/',
        'https://travel.yandex.ru/',
        'https://www.vseinstrumenti.ru/',
        'https://vk.com/',
        ]


def download(url):
    response = requests.get(url)
    dir_path = os.getcwd() + "\\les_4\\task_2\\"
    filename = dir_path + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == "__main__":    
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()

