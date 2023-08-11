from flask import Blueprint, render_template, redirect
from app.forms.login_form import LoginForm
from app.forms.signup_form import SignupForm

bp = Blueprint('session', __name__, url_prefix='/session')

@bp.route('/', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user_info = form.data
    print(user_info)
    return redirect('/')
    
  return render_template('login.html', form=form)
  
@bp.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  if form.validate_on_submit():
    user_info = form.data
    print(user_info)
    return redirect('/')
    
  return render_template('signup.html', form=form)