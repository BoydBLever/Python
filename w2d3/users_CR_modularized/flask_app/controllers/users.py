# users.py
from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash
from flask_app import app


@app.route('/')
def index():
    return render_template('create.html')

@app.route('/create/users', methods=['POST']) #like the middle man, it will get the information from create
def create_user(): #the form from '/' will be sent to this route because it is a post route
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }#the information is captured from the form, we created this dictionary, then we save the whole object
    User.save(data)
    return redirect('/users')


@app.route('/users')
def users():
    return render_template('results.html', users=User.get_all())
    #

