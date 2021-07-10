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
  phone_number = db.Column(db.String, unique=True)
  icon = db.Column(db.String, default='humanicon.jpg')
  #optional: color_id = db.Column(db.String, unique=True)

  dogs = db.relationship("Dog",
                        secondary="users_dogs",
                        backref="users")
  #can access the dogs attribute through users_dogs, don't have to create for Dog class also cause backref
  #optional - check crud functions for accessing users with dogs?
                    
  def __repr__(self):
        return f'<User: user_id={self.user_id} last_name={self.last_name} email={self.email}>'

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
  misc_notes = db.Column(db.String, nullable = True)
  sex=db.Column(db.String)
  breed=db.Column(db.String)
  primary_color=db.Column(db.String)
  microchip_num=db.Column(db.String, nullable=True)
  dob=db.Column(db.DateTime, nullable=True)
  #contacts = db.Column(db.String)

  def __repr__(self):
        return f"<Dog: dog_id={self.dog_id} dog_name={self.dog_name}>"


#users_dogs is the middle for two one-to-many relationships (not actually many to many)
# a dog can have many users. a user can have many dogs. 

class UserDog (db.Model):
  """Relational class that connects a dog of a specific user"""

  __tablename__ = "users_dogs"

  usersdogs_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, 
            db.ForeignKey('users.user_id'),
            nullable=False)
  dog_id = db.Column(db.Integer,
            db.ForeignKey('dogs.dog_id'),
            nullable=False)
  primary_user = db.Column(db.Boolean) #optional - this is just to indicate if someone's the main owner of a dog

  user = db.relationship("User")
  dog = db.relationship("Dog") 

  def __repr__(self):
        return f'<UserDog: dog_id={self.dog_id} user_id={self.user_id}>'

#Questions - relationships vs foreignkey
#to have a relationship, need a foreign key in one table, primary key in another table

#foreignkeys - this column refers to a column in another database table
#relationships - this thing is a reference to another table 
#relationships in sqlalchemy do use foreign keys



# class Task(db.Model):
#   """Tasks to do for the dog"""

#   __tablename__ = "tasks"

#   task_id = db.Column(db.Integer,
#                 autoincrement=True,
#                 primary_key=True)

             
#   dog_id = db.Column(db.Integer,
#             db.ForeignKey('dogs.dog_id'),
#             nullable=False)
#   updated_by = db.Column(db.Integer, 
#             db.ForeignKey('users.user_id'),
#             nullable=False) #references user_id


#   date = db.Column(db.DateTime) #need to check what this date is for
#   task = db.Column(db.String)
#   task_last_occurrence = db.Column(db.DateTime)
#   task_frequency = db.Column(db.DateTime) #unsure if DateTime is the best?




#Questions - check if nullable is default to true or false (which one do you have to specify?)



#----connection----

def connect_to_db(flask_app, db_uri='postgresql:///doglogdb', echo=True):
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