from flask import Blueprint, render_template, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Note
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/play-guess-the-number', methods=['GET', 'POST'])
def play_guess_the_number():
    if request.method == 'GET':
        return render_template('home.html', game_result=None)

    if request.method == 'POST':
        try:
            guess = int(request.form.get('guess'))
            secret_number = 42  
            attempts = 0

            if guess == secret_number:
                game_result = "Congratulations! You guessed the number correctly."
            elif guess < secret_number:
                game_result = "Too low! Try again."
            else:
                game_result = "Too high! Try again."

        except ValueError:
            game_result = "Invalid input. Please enter a valid number."

        return render_template('home.html', game_result=game_result)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note is too short!", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category='success')
            
    user_notes = Note.query.filter_by(user_id=current_user.id).all()

    return render_template("notes.html", user_notes=user_notes)

