from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.user_model import Dojo
from flask_app.models.ninja_model import Ninja
#go to flask_app folder, go to models folder, go to this file, and then import class User

@app.route('/')
def index():
    all_dojos = Dojo.all_dojos() #returns a list of dictionaries
    return render_template('dojos.html', dojos=all_dojos)

@app.route('/dojos', methods=['POST'])
def dojos():
    #take the information from the new dojo form
    data = {
        "name":request.form['name']
    }
    Dojo.create_dojo(data) #returns an id
    return redirect('/')

@app.route('/dojos/<int:id>')
def show_dojo(id):#include id
    all_ninjas = Ninja.all_ninjas()
    return render_template('dojo_show.html', ninjas=all_ninjas)