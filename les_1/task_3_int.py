# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.

from task_2_about import app

@app.route('/sum/<int:num_1>/<int:num_2>/')
def sum_numbers(num_1, num_2):
    return f'Сумма чисел {num_1} и {num_2} равна {num_1 + num_2}'


if __name__ == '__main__':
    app.run()