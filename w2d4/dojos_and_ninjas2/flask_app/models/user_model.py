from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
      

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM users" 
    #     users_from_db = connectToMySQL('users').query_db(query)
        
    #     users = []
    #     for u in users_from_db:
    #         users.append(cls(u))
    #     return users

    # @classmethod
    # def save(cls, data):
    #     query = "Insert INTO users (id, first_name, last_name, email, created_at, updated_at) VALUES (%(id)s, %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
    #     user_id = connectToMySQL('users').query_db(query, data)

    #     return user_id

    @classmethod
    def create_dojo(cls, data): #I know exactly what it is doing with the name
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos