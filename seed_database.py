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


#create json file

# with open('data/users.json') as u:
#   user_data = json.loads(u.read())

# with open('data/users.json') as d:
#   dog_data = json.loads(u.read())

#fake people -----

for n in range(10):
  print(fake.name())


#create 10 fake dogs