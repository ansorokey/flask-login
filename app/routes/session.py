from flask import Blueprint, render_template, redirect
from app.forms.login_form import LoginForm

bp = Blueprint('session', __name__, url_prefix='/session')

@bp.route('/', methods=['GET', 'POST'])
def login
  form = LoginForm()
  if form.validate_on_submit():
    return redirect('/')
  return render_template('login.html', form=form)