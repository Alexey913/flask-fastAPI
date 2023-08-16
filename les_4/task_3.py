# аписать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса. 
#  После загрузки данных нужно записать их в отдельные файлы.
#  Используйте асинхронный подход.

import asyncio
import aiohttp
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


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            dir_path = os.getcwd() + "\\les_4\\task_3\\"
            filename = dir_path + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
                print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")

async def main():
    tasks = []
    for url in urls:
        # task = asyncio.ensure_future(download(url))
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())