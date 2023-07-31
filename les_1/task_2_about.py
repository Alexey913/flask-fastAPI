# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact".


from task_1_hello import app


@app.route('/about/')
def about():
    return 'Информация о чем-либо'


@app.route('/contact/')
def get_contact():
    return """Имя: Алексей</br> \
Фамилия: Шевцов</br> \
Возраст: 32"""


if __name__ == '__main__':
    app.run()