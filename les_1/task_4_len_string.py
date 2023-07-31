# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.


from task_3_int import app


@app.route('/length/<string:string>/')
def length_of_string(string):
    return f'Длина строки "{string}" составляет {len(string)} символов'


if __name__ == '__main__':
    app.run()