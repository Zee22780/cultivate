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


@flashcards.route('/<int:flashcard_id>')
def flashcard(flashcard_id):
  flashcard = Flashcard.query.get_or_404(flashcard_id)
  return render_template('flashcard.html', collection=flashcard.collection, front=flashcard.front, back=flashcard.back, flashcard=flashcard)

@flashcards.route('/<int:flashcard_id>+1')
def next_flashcard(flashcard_id):
  flashcard = Flashcard.query.get_or_404(flashcard_id)
  return render_template('flashcard.html', collection=flashcard.collection, front=flashcard.front, back=flashcard.back, flashcard=flashcard)

@flashcards.route('/<int:flashcard_id>/update', methods=['GET', 'POST'])
@login_required
def update(flashcard_id):
  flashcard = Flashcard.query.get_or_404(flashcard_id)

  if flashcard.author != current_user:
    abort(403)

  form = FlashcardForm()

  if form.validate_on_submit():
    flashcard.collection = form.collection.data
    flashcard.front = form.front.data
    flashcard.back = form.back.data
    db.session.commit()
    flash('Flashcard Updated')
    return redirect(url_for('flashcards.flashcard', flashcard_id=flashcard.id))

  elif request.method == 'GET':
    form.collection.data = flashcard.collection
    form.front.data = flashcard.front
    form.back.data = flashcard.back

  return render_template('create_flashcard.html', title='Updating', form=form)


@flashcards.route('/<int:flashcard_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_flashcard(flashcard_id):

  flashcard = Flashcard.query.get_or_404(flashcard_id)
  if flashcard.author != current_user:
    abort(403)

  db.session.delete(flashcard)
  db.session.commit()
  flash('Flashcard Deleted')
  return redirect(url_for('core.index'))


