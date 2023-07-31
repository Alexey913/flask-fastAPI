# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

from task_4_len_string import app


@app.route('/first_html')
def html_page():
    html = """
    <h1>Моя первая HTML страница</h1>
    <p>Привет, мир!</p>
    """
    return html


if __name__ == '__main__':
    app.run()
