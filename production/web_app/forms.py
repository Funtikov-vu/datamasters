
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField, validators
from wtforms.validators import DataRequired, Length, InputRequired


class FullCardioForm(FlaskForm):


    age = IntegerField('Возраст', [InputRequired()])
    height = IntegerField('Рост', [InputRequired()])
    weight = IntegerField('Вес', [InputRequired()])
    ap_hi = IntegerField('Верхнее кровяное давление', [InputRequired()])
    ap_lo = IntegerField('Нижнее кровяное давление', [InputRequired()])

    gender = SelectField('Пол', [DataRequired()],
                        choices=[(0, 'Мужской'),
                                 (1, 'Женский')])
    alco = SelectField('Алкоголь', [DataRequired()],
                        choices=[(0, 'Не употребляю'),
                                 (1, 'Употребляю')])
    smoke = SelectField('Курение', [DataRequired()],
                        choices=[(0, 'Не курю'),
                                 (1, 'Курю')])
    active = SelectField('Активный образ жизни', [DataRequired()],
                        choices=[(0, 'Не веду'),
                                 (1, 'Веду')])
    cholesterol = SelectField('Холестерин', [DataRequired()],
                        choices=[(1, 'Нормальный'),
                                 (2, 'Повышенный'),
                                 (3, 'Сильно повышенный')])
    gluc = SelectField('Глюкоза', [DataRequired()],
                        choices=[(1, 'Нормальная'),
                                 (2, 'Повышенная'),
                                 (3, 'Сильно повышенная')])

    submit = SubmitField('Отправить')

class UserCardioForm(FlaskForm):


    age = IntegerField('Возраст', [InputRequired()])
    height = IntegerField('Рост', [InputRequired()])
    weight = IntegerField('Вес', [InputRequired()])
    ap_hi = IntegerField('Верхнее кровяное давление', [InputRequired()])
    ap_lo = IntegerField('Нижнее кровяное давление', [InputRequired()])

    gender = SelectField('Пол', [DataRequired()],
                        choices=[(0, 'Мужской'),
                                 (1, 'Женский')])
    alco = SelectField('Алкоголь', [DataRequired()],
                        choices=[(0, 'Не употребляю'),
                                 (1, 'Употребляю')])
    smoke = SelectField('Курение', [DataRequired()],
                        choices=[(0, 'Не курю'),
                                 (1, 'Курю')])
    active = SelectField('Активный образ жизни', [DataRequired()],
                        choices=[(0, 'Не веду'),
                                 (1, 'Веду')])

    submit = SubmitField('Отправить')

class ChooseModelForm(FlaskForm):

    submit_full = SubmitField('Полная модель')
    submit_user = SubmitField('Модель без анализов')