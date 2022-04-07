from flask import Flask, render_template, request, redirect
from balance import get_user_balance


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/get_balance')
def get_balance():

    username = request.args.get('username')

    if username == 'cust1':
        customerID = 6748972358
    else:
        customerID = 6779654690

    balance = get_user_balance(customerID)

    return render_template('balance_envies.html', balance=balance)