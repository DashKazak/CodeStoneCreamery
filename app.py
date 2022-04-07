from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/balance')
def get_balance():
    return render_template('balance_envies.html')