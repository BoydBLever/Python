from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    print(request.form)
    #Registration Validations
    if User.validate_user(request.form):
        print("Validation success")
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
        data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
        }
        #call the save @classmethod on User
        user_id = User.save(data) 
        #store user id into session
        session['user_id'] = user_id 
        return redirect('/recipes')
    else:
        print("Validation fails")
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    #Login Authentications
    #see if the username provided exists in the database
    data = {
        "email" : request.form["email"]
        }
    user_in_db = User.get_by_email(data)
    print(user_in_db)
    print(request.form['user_password'])
    print("^^^^^^^^^^^^^")
    #user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')

    if not bcrypt.check_password_hash(user_in_db.password, request.form['user_password']):
        flash("Invalid Email/Password")
        return redirect('/')
        # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
        #never render on a post
    return redirect('/recipes')
    
@app.route('/recipes')
def recipes():
    data = {
        "id" : session['user_id']
        }
    user = User.get_user_by_id(data) #users[0]
    recipe = Recipe.get_all_recipes(data)
    return render_template('recipes.html', user=user, recipes=recipe)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/recipes/new')
def newrecipe():
    return render_template('newrecipe.html')

@app.route('/createrecipe', methods=['POST'])
def create_recipe():
    data = {
        "name":request.form['name'],
        "description": request.form['description'],
        "under_30":request.form['under_30'],
        "instruction":request.form['instruction'],
        "user_id":session['user_id']
    }
    recipe = Recipe.create_a_recipe(data)
    return redirect('/recipes')