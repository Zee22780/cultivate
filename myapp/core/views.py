# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Flashcard

core = Blueprint('core', __name__)

@core.route('/')
def index():
    flashcards = Flashcard.query
    return render_template('index.html', flashcards=flashcards)

@core.route('/info')
def info():
    return render_template('info.html')