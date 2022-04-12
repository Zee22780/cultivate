# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Flashcard
from myapp.quotes import Quotes


core = Blueprint('core', __name__)

QUOTES = Quotes()

@core.route('/')
def index():
    flashcards = Flashcard.query
    return render_template('index.html', flashcards=flashcards, QUOTES=QUOTES)

@core.route('/info')
def info():
    return render_template('info.html')