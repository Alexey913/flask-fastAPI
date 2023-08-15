from flask import Flask, render_template, request
from task_4.models import db, User
from task_4.forms import RegistrationForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY']=b'7a11a569dc37d6df1a6f75d743fc4590cc2ad62e59096ab1e2a9efc0c1ca36d4'
db.init_app(app)


@app.route('/')
def hello():
    return 'Hi'

@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        existing_user = User.query.filter((User.name == name) | (User.email == email)).first()
        # existing_user = User.query.filter_by(name=user)
        if existing_user:
            error_msg = 'Пользователь с таким именем или email уже существует!'
            form.name.errors.append(error_msg)
            return render_template("registration.html", form=form, title='Регистрация')
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return render_template("registration_sucsess.html", title='Регистрация завершена')
    return render_template("registration.html", form=form, title='Регистрация')


if __name__ == "__main__":
    app.run(debug=True)