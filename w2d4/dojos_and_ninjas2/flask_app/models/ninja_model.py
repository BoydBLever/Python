from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_ninjas(cls, data): #all ninjas at one particular dojo, NOT all of the ninjas in terms of population
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append(ninja)
        return ninjas

    @classmethod
    def new_ninja(cls, data): #I know exactly what it is doing with the name
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results