from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)
csrf = CSRFProtect(app)

class TransferForm(FlaskForm):
    amount = StringField('Cantidad-', validators=[DataRequired()])
    submit = SubmitField('Transferir')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TransferForm()
    # Valor del saldo asignado
    session['balance'] = 1000

    if form.validate_on_submit():
        session['balance'] -= int(form.amount.data)
        return redirect(url_for('transfer_success'))
    return render_template('index.html', form=form)

@app.route('/transfer-success', methods=['GET', 'POST'])
def transfer_success():
    return render_template('transfer.html')

@app.errorhandler(400)
def handle_csrf_error(e):
    return render_template('csrf_error.html'), 400

if __name__ == '__main__':
    app.run(debug=True)
