from The_Recipe_Archives.config.mysqlconnection import connectToMySQL

from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

        # used to model the class after the table from database
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # //classmethod saves user to database
    @classmethod
    def save_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())'
        return connectToMySQL('recipe_project').query_db(query, data)

        # used to check if user in already in databse for login/registration
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("recipe_project").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

        # used to get user data with id saved in session
    @classmethod
    def get_one_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL("recipe_project").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

        # used to validate user info at registration
    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("!*First name must be at least 2 characters.*!")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("!*Last name must be at least 2 characters.*!")
            is_valid = False
        if len(data['password']) < 8:
            flash("!*Password must be at least 8 characters.")
            is_valid = False
        elif not data['password'] == data['confirm_password']:
            flash("!*Password is not a match*!")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("!*Invalid email address!*!")
            is_valid = False
        return is_valid
