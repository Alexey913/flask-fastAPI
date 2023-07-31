# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import render_template
from dataclasses import dataclass
from datetime import date

from task_6_students import app


@dataclass
class News:
    title: str
    text: str
    date: str


@app.route('/news/')
def public_news():

    news_list = [News('Новость 1', 'Описание новости 1', '01.02.2022'),
                 News('Новость 2', 'Описание новости 2', '01.03.2022'),
                 News('Новость 3', 'Описание новости 3', '02.04.2022'),
                 News('Новость 4', 'Описание новости 4', '03.04.2022')
                 ]

    # context = {'students': students_list}
    # return render_template('les_1_task_6.html', **context)
    return render_template('task_7_news.html', news=news_list)


if __name__ == '__main__':
    app.run(debug=True)
