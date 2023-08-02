# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('hw_index.html', title='Главная')


@app.route('/clothes/')
def clothes():
    return render_template('hw_cloth.html', title='Одежда')

@app.route('/about/')
def about():
    return render_template('hw_about.html', title='О нас')


@app.route('/shoes/')
def shoes():
    return render_template('hw_shoes.html', title='Обувь')


@app.route('/jacket/')
def jacket():
    return render_template('hw_jacket.html', title='Куртка')

if __name__ == '__main__':
    app.run(port=8900, debug=True)