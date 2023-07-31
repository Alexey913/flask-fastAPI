# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('task_8_index.html', title='Супер-сайт')


@app.route('/about/')
def about():
    return render_template('task_8_about.html', title='О нас')


@app.route('/contacts/')
def contacts():
    return render_template('task_8_contacts.html', title='Контакты')


if __name__ == '__main__':
    app.run(port=8900)