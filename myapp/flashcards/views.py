from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import Flashcard
from myapp.flashcards.forms import FlashcardForm

flashcards = Blueprint('flashcards', __name__)