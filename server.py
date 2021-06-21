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
    """view all users (*this will not be public)"""

    users=crud.return_all_users()

    return render_template("all_users.html", users=users)

@app.route('/users/<user_id>') 
def userprofile(user_id):
    """view your user profile"""

    user = crud.get_user_by_id(user_id)
    userdogs = crud.get_dog_by_user(user_id) 
    
    return render_template("user_profile.html", user=user, userdogs=userdogs)

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

    print('\n\n\n *********')
    print(email)
    print(password)

    user = crud.get_user_by_email(email)
    if not user or user.password != password: #why use 'if not'?
        flash("The email or password is incorrect")
    else:
        session["user_email"] = user.email
        flash(f"Welcome back, {user.first_name}")
    
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


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
