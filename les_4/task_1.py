#  Написать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса.
#  После загрузки данных нужно записать их в отдельные файлы.
#  Используйте потоки.

import requests
import threading
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
    dir_path = os.getcwd() + "\\les_4\\task_1\\"
    filename = dir_path + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")


threads = []
start_time = time.time()

if __name__ == "__main__":
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

