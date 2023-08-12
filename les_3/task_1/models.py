# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.


from flask_sqlalchemy import SQLAlchemy
from enum import Enum as PyEnum

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(80), nullable=False)
    student_surname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)


    def __repr__(self):
        return f'Student({self.student_name} {self.student_surname} - {self.group})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(120), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)


    def __repr__(self):
        return f'Faculty({self.faculty_name})'