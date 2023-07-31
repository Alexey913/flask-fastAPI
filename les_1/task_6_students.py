# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import render_template
from task_5_html import app


@app.route('/students/')
def get_students():
    
    student_list = [
        {"first_name": "Sam", "last_name": "Winchester", "age": 25, "score": 5},
        {"first_name": "Din", "last_name": "Winchester", "age": 29, "score": 3},
        {"first_name": "Kas", "last_name": "Angel", "age": 1000, "score": 4},
        {"first_name": "Crowly", "last_name": "Demon", "age": 624, "score": 2}
    ]

    # context = {'students': students_list}
    # return render_template('les_1_task_6.html', **context)
    return render_template('task_6_students.html', students = student_list)


if __name__ == '__main__':
    app.run(debug=True)