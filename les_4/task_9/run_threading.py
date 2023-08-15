# Написать программу, которая скачивает изображения с заданных URL-адресов и 
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном 
# файле, название которого соответствует названию изображения в URL-адресе. 
#  Например URL-адрес: https://example/images/image1.jpg -> файл на диске: 
# image1.jpg 
#  Программа должна использовать многопоточный, многопроцессорный и 
# асинхронный подходы.
#  Программа должна иметь возможность задавать список URL-адресов через 
# аргументы командной строки.
#  Программа должна выводить в консоль информацию о времени скачивания 
# каждого изображения и общем времени выполнения программы.


import load_image
import threading
import time
import os

threads = []


def run(url):
    path = os.path.join(os.getcwd(), url.replace('https://','').replace('.', '_').replace('/', ''))
    imgs = load_image.get_all_images(url)
    start_total_time = time.time()
    for img in imgs:
        thread = threading.Thread(target=load_image.download, args=[img, path])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    total_time = time.time() - start_total_time
    for i in range(len(load_image.time_list)):
        print(load_image.time_list[i])
    print(f"Общее время выполнения загрузки - {total_time:.2f} секунды")

if __name__ == "__main__":
    run('https://gb.ru/')
    
    