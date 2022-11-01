from flask import Flask, render_template
app=Flask(__name__)


@app.route('/play') #level 1
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)