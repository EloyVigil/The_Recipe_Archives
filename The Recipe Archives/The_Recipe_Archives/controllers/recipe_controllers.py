from flask import render_template, redirect, request, session, flash

from The_Recipe_Archives import app

from The_Recipe_Archives.models.recipe_models import Recipe

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


