from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms import BooleanField, SelectField, IntegerField, DateTimeField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, EqualTo
from werkzeug.datastructures import FileMultiDict;


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('INGRESAR')
    remember_me = BooleanField('Remember Me')


class TrainingForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    start = StringField('Inicio', validators=[DataRequired()])
    end = StringField('Fin', validators=[DataRequired()])
    description = StringField('Descripcion', validators=[DataRequired()])
    comments = StringField('Comentarios')
    times = SelectField('Horarios', choices=[(1, '8 a 13'), (2, '13 a 18'), (3, '18 a 22')])
    department = SelectField('Sector', choices=[(1, 'DDPyT'), (2, 'DPyPP'), (3, 'DHyA'),(4,'DeSaCo')])


class ClassForm(FlaskForm):
    date = DateField('Inicio', validators=[DataRequired()])
    topics = StringField('Temas vistos', validators=[DataRequired()])
    topicsNext = StringField('Temas Proxima', validators=[DataRequired()])
    comments = StringField('Comentarios')


class TrainerForm(FlaskForm):
    trainer = SelectField('trainer', validators=[DataRequired()], coerce=int)


class StudentForm(FlaskForm):
    file = IntegerField('Legajo', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    surname = StringField('Apellido', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired()])
    degree = StringField('Carrera', validators=[DataRequired()])


class SearchStudentForm(FlaskForm):
  search = SelectMultipleField('search', validators=[DataRequired()], coerce=int)
  submit = SubmitField('Buscar',
                       render_kw={'class': 'btn btn-success btn-block'})

    
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(),Length(min=6, max=35)])
    password = PasswordField('Contrase&ntildea', validators=[
        DataRequired(),
        EqualTo('confirm', message='Las contrase&ntildeas no coinciden')
    ])
    confirm = PasswordField('Repetir contrase&ntildea')
    role = SelectField('Rol', validators=[DataRequired()], coerce=int)
