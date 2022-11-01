from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "rootroot"


@app.route('/')
def index():

    if 'counter' in session:
        session['counter'] += 1
    else:  # else have to have colons after them
        session['counter'] = 1
    return render_template('index.html')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
