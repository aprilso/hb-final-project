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


os.system('dropdb users')
os.system('createdb users')

model.connect_to_db(server.app)
model.db.create_all()

# fake dog names from  from https://github.com/sindresorhus/dog-names 

#create json file

# with open('data/users.json') as u:
#   user_data = json.loads(u.read())


#fake people -----

for n in range(10):

  first_name = fake.first_name()
  last_name = fake.last_name()
  password = fake.password()
  email = fake.last_name()+f"user{n}"+"@email.com"
  phone_number = fake.phone_number()
  icon = "default_icon.jpg"

#how to make parts of this null or go to default? do I specify default here or in crud.py?
  db_user = crud.create_user(first_name, last_name, email, password, phone_number, icon)


#fake dogs ---------

with open('data/male-dog-names.json') as d:
  dog_data = json.loads(d.read())
#question - when/how to use with?

#old version - create 10 fake dogs and giving them color names
# for i in range(10):
#   print(fake.color_name())

#what's the best way to create fake dogs?
dogs_in_db = []
for dog in dog_data:
  dog_name= dog #I think this is the correct way to access the json file?
  photo = "default_dog.jpg"
  bio = "Add your dog's bio here (optional)"
  medication = "Add your dog's medication here (optional) "
  medical_info = "Add your dog's medical info here (optional)" 
  allergies = "Add your dog's allergies here (optional)" 
  weight = "Add your dog's weight here (optional)" #actually this would be an integer 
  food = "Add your dog's food here (optional)" 
  misc_notes = "Add any other miscellaneous notes about your dog here (optional) "

  db_dogs = crud.create_dog(dog_name, photo, bio, medication, medical_info, allergies, weight, food, misc_notes)

# how to fake connect people to dogs???