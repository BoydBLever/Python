from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.user_model import User
#go to flask_app folder, go to models folder, go to this file, and then import class User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('results.html', users=User.get_all())

@app.route('/create/user', methods=['POST'])
def create_user():
        data= {
            "first_name":request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "created_at":request.form['created_at'],
            "updated_at":request.form['updated_at']
        }
        User.save(data)
        return redirect('/users')
