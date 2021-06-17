"""Server for dog logging app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "thiswillbeasecretkey" #Question - ask how this works
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

    return render_template("user_details.html", user=user)

@app.route('/dogs')
def alldogs():
    """view all dogs (*this will not be public)"""

    dogs=crud.return_all_dogs()

    return render_template("all_dogs.html", dogs=dogs)


@app.route('/dog/<dog_id>') 
def dogprofile():
    """view the dog's profile"""

    dog = crud.get_dog_by_id(dog_id)

    return render_template("dog_profile.html", dog=dog)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
