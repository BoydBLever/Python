from flask_app import app
from flask_app.controllers import user_controller
#lines should reflect this particular project's folder and file structure

if __name__=="__main__":
    app.run(debug=True)