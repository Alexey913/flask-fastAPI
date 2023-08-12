from flask import Flask, render_template
from task_1.models import db, Faculty, Student
from random import randint as rnd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)


@app.route('/')
def hello():
    return 'Hi'

@app.cli.command('init-db')
def init_db():
    db.create_all()

@app.cli.command('fill-student')
def fill_students():
    count = 5
    gender_list = ['f', 'm']
    for i in range(1, count+1):
        faculty = Faculty(faculty_name=f'faculty_{i}')
        db.session.add(faculty)
    for i in range(1, count ** 2 + 1):
        stud = Student(
            student_name = f'name_{i}',
            student_surname = f'surname_{i}{i}',
            age = rnd(17, 30),
            gender = gender_list[rnd(0,1)],
            group = rnd(1, count),
            faculty_id = rnd(1, 5)
        )
        db.session.add(stud)
    db.session.commit()


@app.route('/get_data/')
def get_data():
    students = Student.query.all()
    return render_template('students.html', students = students, title = 'Students')


if __name__ == "__main__":
    app.run(debug=True)