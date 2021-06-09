"""CRUD operations (Create Read Update Delete) """

from model import db, User, Dog, connect_to_db
from datetime import datetime

def create_user(first_name, last_name, email, password, phone_number, icon):
  """Create and return a new user."""

  user = User(first_name=first_name, last_name=last_name, email=email, password=password, phone_number=phone_number, icon=icon)

  db.session.add(user)
  db.session.commit()

  return user

def return_all_users():
    """return all human users"""
    return User.query.all()

def get_user_by_id(user_id):
    """look up the user by id"""
    return User.query.get(user_id)

def get_user_by_email(email):
    """return a user by email"""
    return User.query.filter(User.email == email).first()


def create_dog(dog_id, dog_name, photo, bio, medication, medical_info, allergies, weight, food, misc_notes):
  """Create and return a new dog."""

  dog = Dog(dog_id=dog_id, dog_name=dog_name, photo=photo, bio=bio, medication=medication, medical_info=medical_info, allergies=allergies, weight=weight, food=food, misc_notes=misc_notes)

  db.session.add(dog)
  db.session.commit()

  return dog

def get_dog_by_id(dog_id):
    """look up the user by id"""
    return Dog.query.get(dog_id)