"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

from faker import Faker
fake = Faker()

import crud
import model
import server

os.system('dropdb doglogdb') #might have failed if something else was accessing the database
os.system('createdb doglogdb')


model.connect_to_db(server.app)
model.db.create_all()

# fake dog names from  from https://github.com/sindresorhus/dog-names 

#fake people ----- 

for n in range(10):
  first_name = fake.first_name()
  last_name = fake.last_name()
  password = fake.password()
  email = last_name +f"_user{n}"+"@gmail.com"
  phone_number = fake.phone_number()
  icon = "default_icon.jpg"

#how to make parts of this null or go to default? do I specify default here or in crud.py?
  db_user = crud.create_user(first_name, last_name, email, password, phone_number, icon)

#fake dogs ---------

with open('data/male-dog-names.json') as d: #"with" opens the file, closes it for you
  dog_data = json.loads(d.read())

  dogs_in_db = []

#To-Do: add plausible (random choice) data for each of these
  for dog in dog_data:
    dog_name= dog 
    photo = "default_dog.jpg"
    bio = "Add your dog's bio here (optional)"
    medication = "Add your dog's medication here (optional) "
    medical_info = "Add your dog's medical info here (optional)" 
    allergies = "Add your dog's allergies here (optional)" 
    weight = randint(10,75)
    food = "Add your dog's food here (optional)" 
    misc_notes = "Add any other miscellaneous notes about your dog here (optional) "
    sex = choice("MF")
    breed = choice(["Labradoodle","Pug", "Mixed", "Chow Chow", "Terrier Mix"])
    primary_color = choice(["Yellow", "Black", "White", "Brown"])
    microchip_num = "NONE"

    db_dog = crud.create_dog(dog_name, photo, bio, medication, medical_info, allergies, weight, food, misc_notes, sex, breed, primary_color, microchip_num)

    dogs_in_db.append(db_dog)

    #create an instance of UserDog class using the primary id of the dog and user that was just created
    user_id = randint(1,10)
    dog_id = db_dog.dog_id
    primary_user = True #the user can be primary user for multiple dogs  

    db_userdog = crud.assign_dog_to_human(user_id, dog_id, primary_user)

