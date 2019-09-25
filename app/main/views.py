
from flask import render_template
from . import main

@main.route('/')
def index():
    title='welcome to women Tech site'
    return """
    <h1>Hello world!</h1>

    <iframe src="https://www.youtube.com/embed/XebNxUE3ugA" width="890" height="500" frameborder="0" allowfullscreen></iframe>
    """

@main.route('motive')
def motive():
    return render_template("motive.html")

