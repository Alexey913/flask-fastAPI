# Создать базу данных для хранения информации о книгах в библиотеке.
#  База данных должна содержать две таблицы: "Книги" и "Авторы".
#  В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
#  В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
#  Необходимо создать связь между таблицами "Книги" и "Авторы".
#  Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
    authors = db.relationship('Author', secondary='book_author', backref="book", lazy=True)

    def __repr__(self):
        return f'{self.title} - {self.authors}'


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))