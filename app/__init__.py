from flask import Flask, render_template
from app.config import Config
from app.models import db, User
from app.routes import session
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(session.bp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "session.login"

db.init_app(app)
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/')
def index():
  return render_template('index.html')
