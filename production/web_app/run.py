import sys
import os
import logging


from werkzeug.utils import redirect

sys.path.append(".")

from flask import Flask, render_template, request, url_for, jsonify
from forms import FullCardioForm, UserCardioForm, ChooseModelForm
from api_server.predict import predict

app = Flask(__name__)

app.config['SECRET_KEY'] = '42'

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/", methods=['GET', 'POST'])
def choose_model():
    form_choose = ChooseModelForm(request.form)
    if request.method == 'POST':

        # validate
        if form_choose.validate():
            if 'submit_full' in request.form:
                return redirect(url_for('main_cardio_check'))
            elif 'submit_user' in request.form:
                return redirect(url_for('user_cardio_check'))

    return render_template('choose_model.html', form=form_choose)


@app.route("/main_cardio_check", methods=['GET', 'POST'])
def main_cardio_check():
    submission_successful = False
    predict_value = 0
    scroll = False
    form = FullCardioForm(request.form)
    if request.method == 'POST':

        # validate
        if form.validate():
            age = int(request.form['age'])
            gender = int(request.form['gender'])
            height = int(request.form['height'])
            weight = int(request.form['weight'])
            ap_hi = int(request.form['ap_hi'])
            ap_lo = int(request.form['ap_lo'])
            smoke = int(request.form['smoke'])
            alco = int(request.form['alco'])
            active = int(request.form['active'])
            cholesterol = int(request.form['cholesterol'])
            gluc = int(request.form['gluc'])
            bmi = weight / ((height / 100) ** 2)
            diff = ap_hi - ap_lo
            cholesterol_1 = int(cholesterol == 1)
            cholesterol_2 = int(cholesterol == 2)
            cholesterol_3 = int(cholesterol == 3)
            gluc_1 = int(gluc == 1)
            gluc_2 = int(gluc == 2)
            gluc_3 = int(gluc == 3)
            submission_successful = True
            scroll = 1
            predict_value = predict(
                {'age': age, 'gender': gender, 'height': height, 'weight': weight, 'ap_hi': ap_hi, 'ap_lo': ap_lo,
                 'smoke': smoke, 'alco': alco, 'active': active, 'bmi': bmi, 'diff': diff,
                 'cholesterol_1': cholesterol_1, 'cholesterol_2': cholesterol_2, 'cholesterol_3': cholesterol_3,
                 'gluc_1': gluc_1, 'gluc_2': gluc_2, 'gluc_3': gluc_3}, 'main')

    return render_template('full_cardio_form.html', form=form, submission_successful=submission_successful,
                           predict=predict_value, scroll=scroll)


@app.route("/user_cardio_check", methods=['GET', 'POST'])
def user_cardio_check():
    submission_successful = False
    predict_value = 0
    scroll = False
    form = UserCardioForm(request.form)
    if request.method == 'POST':

        # validate
        if form.validate():
            age = int(request.form['age'])
            gender = int(request.form['gender'])
            height = int(request.form['height'])
            weight = int(request.form['weight'])
            ap_hi = int(request.form['ap_hi'])
            ap_lo = int(request.form['ap_lo'])
            smoke = int(request.form['smoke'])
            alco = int(request.form['alco'])
            active = int(request.form['active'])
            bmi = weight / ((height / 100) ** 2)
            diff = ap_hi - ap_lo
            submission_successful = True
            scroll = 1
            predict_value = predict(
                {'age': age, 'gender': gender, 'height': height, 'weight': weight, 'ap_hi': ap_hi, 'ap_lo': ap_lo,
                 'smoke': smoke, 'alco': alco, 'active': active, 'bmi': bmi, 'diff': diff}, 'user')

    return render_template('user_cardio_form.html', form=form, submission_successful=submission_successful,
                           predict=predict_value, scroll=scroll)

@app.route('/user', methods=['GET'])
def get_cardio_user():
    return jsonify({'cardio': predict(request.json, 'user')})


@app.route('/main', methods=['GET'])
def get_cardio_main():
    return jsonify({'cardio': predict(request.json, 'main')})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
