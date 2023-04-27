from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    # Valor del saldo asignado
    session['balance'] = 1000
    return render_template('index.html')

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    session['balance'] -= int(amount)
    # Retornar el saldo restante
    return "Success. Saldo restante: {}.".format(session['balance'])

if __name__ == '__main__':
    app.run(debug=True)
