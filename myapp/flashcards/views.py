from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import Flashcard
from myapp.flashcards.forms import FlashcardForm

flashcards = Blueprint('flashcards', __name__)

@flashcards.route('/create', methods=['GET', 'POST'])
@login_required
def create_flashcard():
  form = FlashcardForm()
  if form.validate_on_submit():
    flashcard = Flashcard(collection=form.collection.data, front=form.front.data, back=form.back.data, user_id=current_user.id)
    db.session.add(flashcard)
    db.session.commit()
    flash('Flashcard Created')
    print('Flashcard Created')
    return redirect(url_for('core.index'))
  return render_template('create_flashcard.html', form=form)