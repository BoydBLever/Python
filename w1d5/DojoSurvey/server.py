from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'rootroot'

@app.route('/') #line 5 route is a GET #Form is sending a POST request to line 9 route
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST']) 
def results():
    print(request.form) #it's a dictionary; populates in the terminal.
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/display') #never render on a post method

@app.route('/display')
def display():
    return render_template("display.html")

if __name__== "__main__":
    app.run(debug=True)
