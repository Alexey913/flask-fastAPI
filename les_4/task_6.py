# Создать программу, которая будет производить подсчет 
# количества слов в каждом файле в указанной директории и 
# выводить результаты в консоль.
# Используйте асинхронный подход..

import asyncio
import aiofiles
import time
import os


# async def count_word(file, folder):
#     count = 0
#     filename = os.path.join(folder, file)
#     if os.path.isfile(filename):
#         with open(filename, "r", encoding='utf-8') as f:
#             for line in f:
#                 count+=len(line.split())
#         with open("./les_4/task_6.txt", "a", encoding='utf-8') as res:
#             res.write(file + " - количество слов: " + str(count) + "\n")
#             print(f"Подсчет слов в файле {file} за {time.time()-start_time:.2f} секунд")


async def count_word(file, folder):
    count = 0
    filename = os.path.join(folder, file)
    if os.path.isfile(filename):
        async with aiofiles.open(filename, "r", encoding='utf-8') as f:
            content = await f.read()
            count+=len(content.split())
        with open("./les_4/task_6.txt", "a", encoding='utf-8') as res:
            res.write(file + " - количество слов: " + str(count) + "\n")
            print(f"Подсчет слов в файле {file} за {time.time()-start_time:.2f} секунд")

async def main():
    tasks = []

    files=os.listdir(folder)
    for file in files:
        task = asyncio.create_task(count_word(file, folder))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()
folder = os.getcwd() + "\\les_2\\templates"

if __name__ == "__main__":
    asyncio.run(main())
