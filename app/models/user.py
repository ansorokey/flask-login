from app.models import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Columm(db.String(30), nullable=False)
  password = db.Column(db.String(30), nullable=False)
  
  # The flask_sqlalchemy package comes with many time savings dependancies that would otherwise be their own imports
  # When creating a mapped class, we xould also declare columns and types by explicitly importing them
  # Both provide the same functionality. This is a matter of preference
  """
  from sqlalchemy.schema import Column
  from sqlalchemy.types import Integer, String
  
  class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Columm(String(30), nullable=False)
    password = Column(String(30), nullable=False)
  """