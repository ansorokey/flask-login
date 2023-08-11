A generic template to get an understanding of how the flask-login package works.

This is a mofified version of an online tutorial to better match the contemt and style learned in App Academy. Original tutorial can be found [here](https://youtu.be/71EU8gnZqZQ).

## Notice Regarding Files
A `.env` and `.flaskenv` file were excluded from the `.gitignore` file for study purposes. Please remember to include them in the `.gitignore` of future projects.

## Relevant Documentation
[Flask Login](https://flask-login.readthedocs.io/en/latest/)

[Form Fields]()

## Packages Used
Flask
Flask SQLAlchemy
Flask Login

## Terminal Commands
### Installing packages
pipenv install flask flask_sqlalchemy sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator jinja2 python-dotenv alembic Flask-Migrate

### Initialize database and migration files
pipenv run flask db init

### Migrate database
pipenv run flask db migrate -m "create packages table"
pipenv run flask db upgrade

### Running application
pipenv run flask run
