from flask_app.config.mysqlconnection import connectToMySQL
#create the Recipe class
class Recipe:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.under_30=data['under_30']
        self.instruction=data['instruction']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        
    @classmethod
    def create_a_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, under_30, instruction, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(under_30)s, %(instruction)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL("recipes").query_db(query,data)
    
    @classmethod
    def get_all_recipes(cls,data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL("recipes").query_db(query,data)
        recipes = []
        for recipe in results:
            recipes.append(recipe)
        return recipes


