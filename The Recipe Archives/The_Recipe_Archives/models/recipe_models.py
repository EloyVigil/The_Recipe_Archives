from The_Recipe_Archives.config.mysqlconnection import connectToMySQL

from flask import flash


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.instructions = data['instructions']
        self.ingredients = data['ingredients']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes (name, instructions, ingredients, created_at, updated_at, user_id) VALUES(%(name)s, %(instructions)s, %(ingredients)s NOW(), NOW(), %(user_id)s);"
        print(data)
        return connectToMySQL('recipe_project').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        results = connectToMySQL('recipe_project').query_db(query, data)
        return results
