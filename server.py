"""Server for dog logging app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "thiswillbeasecretkey" #Used to encrypt a session. Can set it to generate random #s and letters each time, or in secrets.sh (make more secret before deployment)
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """view homepage"""
    return render_template('homepage.html')


@app.route('/users')
def allusers():
    """view all users"""

    users=crud.return_all_users()

    return render_template("all_users.html", users=users)

@app.route('/users/<user_id>') 
def userprofile(user_id):
    """view a user profile"""

    user = crud.get_user_by_id(user_id)
    userdogs = crud.get_dog_by_user(user_id) 
    
    return render_template("user_profile.html", user=user, userdogs=userdogs)
    # NOTE: or is it render template your_profile.html?

@app.route('/dogs')
def alldogs():
    """view all dogs (*this will not be public)"""

    dogs=crud.return_all_dogs()

    return render_template("all_dogs.html", dogs=dogs)


@app.route('/dogs/<dog_id>') 
def dogprofile(dog_id):
    """view the dog's profile"""

    dog = crud.get_dog_by_id(dog_id)
    userdogs = crud.get_user_by_dog(dog_id)

    return render_template("dog_profile.html", dog=dog, userdogs=userdogs)


@app.route('/login', methods=["POST"])
def login():
    """login user"""
    email = request.form.get('login_email')
    password = request.form.get('login_password')

    user = crud.get_user_by_email(email)
    if not user or user.password != password: #why use 'if not'?
        flash("The email or password is incorrect")
    else:
        session["user_email"] = user.email
        session["user_id"] = user.user_id #in the future, could just store user_id and lookup email from that
        flash(f"Welcome back, {user.first_name}") # TO-DO - redirect to the logged in page instead
    
    return redirect("/")

@app.route('/new_user')
def new_user_page():

    return render_template("new_user.html")

@app.route('/users', methods=["POST"])
def new_user():
    """creates a new user account"""

    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone_number = request.form.get('phone_number')
    icon = 'default_user_icon.jpg'

    new_user = crud.get_user_by_email(email)

    if new_user == None:
        crud.create_user(first_name, last_name, email, password, phone_number, icon)
        flash("Success! New account has been created")
    else:
        flash("An account with that email already exists.")

    return redirect('/')

@app.route('/add_dog', methods=["POST"])
def new_dog_to_user():

    dog_name = request.form.get('dog_name')
    photo = 'default_dog_icon.jpg'
    bio = request.form.get('bio')
    medication = request.form.get('medication')
    medical_info = request.form.get('medical_info')
    allergies = request.form.get('allergies')
    weight = request.form.get('weight')
    food = request.form.get('food')
    misc_notes = request.form.get('misc_notes')
    sex = request.form.get('sex')
    breed = request.form.get('breed')
    primary_color = request.form.get('primary_color')
    microchip_num = request.form.get('microchip_num')

    new_dog = crud.create_dog

    pass


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
