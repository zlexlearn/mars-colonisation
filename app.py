import flask
from flask import render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum'

class LoginForm(FlaskForm):
    astronaut_id = StringField('ID астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    capitan_id = StringField("ID капитана", validators=[DataRequired()])
    capitan_password = StringField("Пароль капитана", validators=[DataRequired()])
    access = SubmitField('Доступ')


@app.route("/")
def main():
    return render_template('base.html')

@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    context = {'prof': prof}
    return render_template('training.html', **context)

@app.route('/promotion')
def promotion():
    return ''

@app.route('/image_mars')
def image_mars():
    return ''

@app.route('/list-prof/<lst>')
def list_prof(lst):
    context = {
        'list': lst,
        'profs': ['инженер', 'пилот', 'врач', 'строитель'] * 100
    }
    return render_template('list_prof.html', **context)

@app.route('/astronaut_selection')
def asselect():
    return ''

@app.route('/answer', methods=['POST'])
@app.route('/auto_answer', methods=['POST'])
def answer():
    context = {
        'surname': request.form['surname'],
        'name': request.form['name'],
        'title': 'Анкета',
        'education': request.form['education'],
        'profession': ', '.join(request.form.getlist('profession')),
        'gender': request.form['gender'],
        'motivation': request.form['motivation'],
        'ready': request.form.get("ready", '') == 'Готов'
    }
    return render_template('answer.html', **context)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html', form=LoginForm())
    elif request.method == 'POST' and LoginForm().validate_on_submit():
        return redirect('/')

app.run('127.0.0.1', 5000)

