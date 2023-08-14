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



import re
import requests
from bs4 import BeautifulSoup

site = 'http://pixabay.com'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)