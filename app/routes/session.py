from flask import Blueprint, render_template, redirect
from app.forms.login_form import LoginForm
from app.forms.signup_form import SignupForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db, User
from flask_login import login_user, login_required, logout_user, current_user

bp = Blueprint('session', __name__, url_prefix='/session')

@bp.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    # search for username in database
    db_user = User.query.filter(User.username == form.data['username']).first()
    # if username found -
    if db_user:
      # check if passwords match
      if check_password_hash(db_user.password, form.data['password']):
        login_user(db_user)
        return redirect('/dashboard')
  return render_template('login.html', form=form)

@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
  logout_user()
  return redirect('/')


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  if form.validate_on_submit():
    hashed_password = generate_password_hash(form.data['password'])
    new_user = User(
      username=form.data['username'],
      password=hashed_password,
      firstname=form.data['first_name'],
      lastname=form.data['last_name']
    )
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return redirect('/dashboard')
  return render_template('signup.html', form=form)
