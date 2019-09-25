from flask import render_template
from . import main

@main.route('/')
def index():
    title='welcome to women Tech site'
    return render_template('index.html',title=title)

@main.route('/motive')
def motive():
    return render_template("motive.html")