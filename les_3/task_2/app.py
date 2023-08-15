import os
import random

from flask import Flask, render_template
from task_2.models import db, Author, Book, BookAuthor
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY']=b'7a11a569dc37d6df1a6f75d743fc4590cc2ad62e59096ab1e2a9efc0c1ca36d4'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///books.db'
db.init_app(app)


@app.route('/')
def index():
    return "hello"


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("add-books")
def add_books():
    for i in range(1, 11):
        book = Book(
            title=f'Book{i}',
            year=f'200{randint(1, i)+10}',
            count=randint(50, 100))
        db.session.add(book)
    db.session.commit()


@app.cli.command("add-authors")
def add_authors():
    for i in range(1, 5):
        author = Author(
            firstname=f'Name{i}',
            lastname=f'Surname{i}')
        db.session.add(author)
    db.session.commit()


@app.cli.command("add-relation")
def add_authors():
    for i in range(1, 20):
        if i > 10:
            i = randint(1, 10)
        b_a = BookAuthor(
            book_id=i,
            author_id=randint(1, 4)
        )
        db.session.add(b_a)
    db.session.commit()


@app.route("/books/")
def books():
    all_books = Book.query.all()
    context = {'books': all_books}
    return render_template("books.html", **context, title="Книги")


if __name__ == "__main__":
    app.run(debug=True)
