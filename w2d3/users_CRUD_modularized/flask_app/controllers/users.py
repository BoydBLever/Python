# users.py
from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash
from flask_app import app


@app.route('/')
def index():
    return render_template('create.html')
# like the middle man, it will get the information from create

@app.route('/create/users', methods=['POST'])
def create_user():  # the form from '/' will be sent to this route because it is a post route
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }  # the information is captured from the form, we created this dictionary, then we save the whole object
    User.save(data)  # I could pass request.form into save, like save(request.form['name'])
    return redirect('/users')


@app.route('/users')
def users():
    return render_template('results.html', users=User.get_all())


@app.route('/users/<int:id>')
def show(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    print(user.first_name)
    return render_template('show.html', user=user)


@app.route('/users/delete/<int:id>')
def delete(id):
    data = {
        "id": id  # id goes into a dictionary called data
    }
    User.remove(data)
    return redirect('/')

@app.route('/users/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": id
    }
    User.update(data)
    return redirect(f'/users/{id}')

@app.route('/users/update/<int:id>', methods=['GET'])
def editpage(id):
    data = {
        "id":id
    }
    return render_template('edit.html', user=data)
