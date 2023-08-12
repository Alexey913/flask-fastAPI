import logging
from flask import Flask, abort, make_response, render_template, request, url_for, redirect, flash, session
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path
from markupsafe import escape


_AGE_LIMIT = 18
logger = logging.getLogger(__name__)
app = Flask(__name__, static_folder='static')
app.secret_key = b'48144ee52bd3424f2daf85dceb41e26eab86f99fcd47206bbd681243c8eaefa5'


@app.route("/")
def index():
    if 'username' in session:
        aut_session = session['username']
    else:
        aut_session = None
    if request.cookies.get('username'):
        aut_cookie = request.cookies.get('username')
    else:
        aut_cookie = None
    return render_template("index.html", title="Главное меню", autorization_session=aut_session, autorization_cookie=aut_cookie)


# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

@app.route("/hello/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        if request.form.get('username'):
            username = request.form.get('username')
        else:
            username = "дружище"
        return render_template("hello_name.html", title=f"Ну, здравствуй, {username}", username=username)
    return render_template("hello.html", title="Приветствие")


# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.


@app.route("/imgload/", methods=['GET', 'POST'])
def imgload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(
            Path.cwd(), 'les_2/static/image', file_name))
        return render_template('image_download.html', file_name=file_name, title="А вот и наша картинка")
    return render_template("image_upload.html", title="Загрузка картинки")


# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.


users = {"admin": "123", "guest": "321"}


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('login')
        password = request.form.get('password')
        if (username, password) in users.items():
            return render_template('enter_sucsess.html', file_name=username, title="Успешный вход")
        else:
            return render_template('enter_error.html', file_name=username, title="Ошибка входа")
    return render_template("enter.html", title="Введите логин и пароль")


# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

@app.route("/word_count/", methods=['GET', 'POST'])
def count_words():
    if request.method == 'POST':
        input_string = request.form.get('text')
        count_words = len(input_string.split())
        return render_template('word_count_result.html', string=input_string, count=count_words, title="Результат подсчета")

    return render_template("word_count.html", title="Подсчет слов в строке")


# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

@app.route("/calculator/", methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        number_1 = int(request.form.get('number_1'))
        number_2 = int(request.form.get('number_2'))
        operation = request.form.get('operation')
        result = 0
        try:
            match operation:
                case 'Сумма':
                    result = number_1 + number_2
                case 'Разность':
                    result = number_1 - number_2
                case 'Произведение':
                    result = number_1 * number_2
                case 'Частное':
                    result = number_1 / number_2
                case _:
                    result = 'Ошибка выбора операции'
            return render_template('calculate_result.html', num_1=number_1, num_2=number_2, oper=operation, res=result, title="Результат вычисления")

        except (ZeroDivisionError):
            return render_template('calculate_result.html', num_1=number_1, num_2=number_2, oper="На 0 делить нельзя! Частное ", res=float('inf'))
    return render_template("calculate.html", title="Калькулятор")


# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


@app.route("/check_age/", methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age < _AGE_LIMIT:
            abort(403)
        return render_template('check_age_result.html', name=name, age=age, title="Результат проверки")
    return render_template("check_age.html", title="Проверка возраста")


@app.errorhandler(403)
def page_acsess_deined(e):
    logger.warning(e)
    context = {
        'title': 'Доступ запрещен!',
        'url': request.base_url,
    }
    return render_template('403.html', **context), 403

# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


@app.route("/redirect_page/", methods=['GET', 'POST'])
def redirect_page():
    if request.method == 'POST':
        num = int(request.form.get('number'))
        result = num ** 2
        return redirect(url_for('square', result=result, num=num))
    return render_template("redirect.html", title="Перенаправление")


@app.route("/redirect_result/")
def square():
    num = request.args.get('num')
    result = request.args.get('result')
    return render_template("redirect_result.html", result=result, number=num, title=f"Квадрат числа {num}")


# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!"


@app.route("/flash/", methods=['GET', 'POST'])
def flash_message():
    if request.method == 'POST':
        username = request.form.get('username')
        if username.isalpha():
            flash(f' Привет, {username}!', 'success')
            return redirect(url_for('flash_message'))
        flash(f'Я не знаю такого имени!', 'error')
        return redirect(url_for('flash_message'))
    return render_template('flash.html', title="Флэш-сообщения")


# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан session файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален session файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

# Для cookie
@app.route("/hw_cookie/", methods=['GET', 'POST'])
def hw_cookie():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        if username != "" and email != "":
            response = make_response(redirect(url_for('login_cookie')))
            response.set_cookie('username', username)
            response.set_cookie('email', email)
            return response
        if username == "":
            flash(f' Введите имя!', 'error')
            return redirect(url_for('hw_cookie'))
        if email == "":
            flash(f' Введите e-mail!', 'error')
            return redirect(url_for('hw_cookie'))
    return render_template('hw_cookie.html', title="cookie-файлы")


@app.route("/login_cookie/", methods=['GET', 'POST'])
def login_cookie():
    username = request.cookies.get('username')
    email = request.cookies.get('email')
    if request.method == 'POST':
        return redirect(url_for('logout_cookie', username=username, email=email))
    return render_template('login_cookie.html', name=username, email=email, title="Личный кабинет cookie")


@app.route("/logout_cookie/")
def logout_cookie():
    response = make_response(redirect(url_for('hw_cookie')))
    response.set_cookie('username', "", max_age=0)
    response.set_cookie('email', "", max_age=0)
    print(request.cookies.get('username'))
    return response


# Для сессии
@app.route("/hw_session/", methods=['GET', 'POST'])
def hw_session():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        if username != "" and email != "":
            session['username'] = username
            session['email'] = email
            return redirect(url_for('login_session'))
        if username == "":
            flash(f' Введите имя!', 'error')
            return redirect(url_for('hw_session'))
        if email == "":
            flash(f' Введите e-mail!', 'error')
            return redirect(url_for('hw_session'))
    return render_template('hw_session.html', title="session-файлы")


@app.route("/login_session/", methods=['GET', 'POST'])
def login_session():
    if request.method == 'POST':
        return redirect(url_for('logout_session'))
    return render_template('login_session.html', name=session['username'], email=session['email'], title="Личный кабинет в сессии")


@app.route("/logout_session/")
def logout_session():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('hw_session'))


if __name__ == '__main__':
    app.run(debug=True)
