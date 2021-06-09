"""Models for dog logging app """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
  """A human user."""

  __tablename__ = "users"

  user_id = db.Column(db.Integer,
                autoincrement=True,
                primary_key=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)
  password = db.Column(db.String)
  phone_number = db.Column(db.Integer, unique=True)
  icon = db.Column(db.String) #default='dog.jpg'
  #optional: color_id = db.Column(db.String, unique=True)

  def __repr__(self):
        return f'<User: user_id={self.user_id} email={self.email}>'

class Dog(db.Model):
  """A dog"""

  __tablename__ = "dogs"

  dog_id = db.Column(db.Integer,
                autoincrement=True,
                primary_key=True)
  dog_name = db.Column(db.String, nullable=False)
  photo = db.Column(db.String) #default='dog.jpg'
  bio = db.Column(db.String, nullable=True)
  medication = db.Column(db.String, nullable=True)
  medical_info = db.Column(db.String, nullable=True)
  allergies = db.Column(db.String, nullable=True)
  weight = db.Column(db.Integer, nullable=True)
  food = db.Column(db.String, nullable=True)
  misc_notes = db.Column(db.String, nullable=True)

def __repr__(self):
        return f'<Dog: dog_id={self.user_id} dog_name={self.dog_name}>'


class Task(db.Model):
  """Tasks to do for the dog"""

  __tablename__ = "tasks"



#Next - check how to make users_dogs table



#Questions - check if nullable is default to true or false (which one do you have to specify?)

#----connection----

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
  flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
  flask_app.config['SQLALCHEMY_ECHO'] = echo
  flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.app = flask_app
  db.init_app(flask_app)

  print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)