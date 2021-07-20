"""CRUD operations (Create Read Update Delete) """

from model import Task, TaskHistory, db, User, Dog, UserDog, connect_to_db
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


def get_user_without_dog(dog_id):
    """return all users without dogs"""
    #To-Do - where their dog_id = null??
    pass



#Note: unwieldy, could take in one dog_info as a dictionary and then key into it 
def create_dog(dog_name, photo, bio, medication, medical_info, allergies, weight, food, misc_notes, sex, breed, primary_color, microchip_num, dob):
  """Create and return a new dog."""

  dog = Dog(dog_name=dog_name, photo=photo, bio=bio, medication=medication, medical_info=medical_info, allergies=allergies, weight=weight, food=food, misc_notes=misc_notes, sex=sex, breed=breed,
        primary_color=primary_color, microchip_num=microchip_num, dob=dob)
  #add vet

  db.session.add(dog)
  db.session.commit()

  return dog

#To-Do - create functions for updating the info for users and dogs (without taking in each variable)
# def update_dog():
#Note: check out ratings lab crud.py


def get_dog_by_id(dog_id):
  """look up the dog by id"""
  return Dog.query.get(dog_id)

def return_all_dogs():
  """return all dogs"""
  return Dog.query.all()

#To-Do: update human info by user_id, update dog info by dog_id

def get_dog_by_user(user_id):
  """get all the dogs that belong to a user"""

  return UserDog.query.filter(UserDog.user_id == user_id).all()
  
def get_user_by_dog(dog_id):
  """get all the users of a single dog"""

  return UserDog.query.filter(UserDog.dog_id == dog_id).all()

def assign_dog_to_human(user_id, dog_id, primary_user):
  """assign a dog to a human""" #should also work for assign human to dog

  userdog = UserDog(dog_id=dog_id, user_id=user_id, primary_user=primary_user)

  db.session.add(userdog)
  db.session.commit()

  return userdog

#TASKS SECTION ----

def create_task(dog_id, task_name, task_created_time, task_frequency, task_scheduled_time, flexible, task_scheduled_day, 
                task_scheduled_hour_start, task_scheduled_hour_end):
  """create a task for a dog (to be completed by the user)"""
  
  task = Task(dog_id=dog_id, task_name=task_name, task_created_time=task_created_time, task_frequency=task_frequency, task_scheduled_time=task_scheduled_time, flexible=flexible, 
        task_scheduled_day=task_scheduled_day, task_scheduled_hour_start=task_scheduled_hour_start, task_scheduled_hour_end=task_scheduled_hour_end)

  db.session.add(task)
  db.session.commit()

  return task

def get_tasks_by_dog(dog_id):
  """return all the tasks that belong to one dog"""

  return Task.query.filter(Task.dog_id == dog_id).all()
  
def mark_task_complete():
  """Update the status of a task - mark an existing dog's task as complete or add notes """
  pass

def return_completed_tasks():
  """return all tasks that have already been completed"""
  pass

def return_all_tasks_until_now():
  """return all tasks up until this datetime"""
  #will reference TaskHistory
  pass







if __name__ == '__main__':
    from server import app
    connect_to_db(app)