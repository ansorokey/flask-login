from flask import Flask, render_template
from app.config import Config
from app.models import db
from app.routes import session

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(session.bp)
db.init_app(app)

@app.route('/')
def index():
  return render_template('index.html')