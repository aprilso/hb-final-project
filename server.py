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
def userprofile():
    """view your user profile"""
    pass

@app.route('/dogs')
def alldogs():
    """view all dogs (*this will not be public)"""
    pass

@app.route('/dog/<dog_id>') 
def dogprofile():
    """view the dog's profile"""
    pass



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
