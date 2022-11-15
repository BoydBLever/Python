from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.password=data['password']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL("recipes").query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL("recipes").query_db(query,data)
        # Didn't find a matching user
        if len(results) < 1:
            return False
        user = cls(results[0])
        return user

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL("recipes").query_db(query,data)
        users = []
        for user in results:
            users.append(cls(user))
        return users[0]

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        #email must have valid email format
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        # password and confirm pw must match
        if user['password'] != user['confirm_password']:
            flash("Confirm password must match password.")
            is_valid = False
        # user must NOT already exist in the DB
        user_in_db = User.get_by_email(user)
        # user is not registered in the db
        if user_in_db:
            flash("Invalid Email/Password")
            is_valid = False
        # if len(User.get_by_email(user)) > 0: #create classmethod get_by_email
        #     flash("User already exists.")
        #     is_valid = False

        return is_valid