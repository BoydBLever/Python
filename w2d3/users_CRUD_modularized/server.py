from flask_app.controllers import users #import users works here but not in other modularized assignments, including dojos and ninjas
from flask_app import app
# ...server.py


if __name__ =="__main__":
    app.run(debug=True)

