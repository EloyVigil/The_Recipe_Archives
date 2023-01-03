from flask import render_template, redirect, request, session, flash

from The_Recipe_Archives import app

from The_Recipe_Archives.models.user_models import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

    # to display the landing page html file
@app.route('/')
def homepage():
    return render_template('homepage.html')

    # used to display user dashboard if user is logged in
@app.route('/dashboard')
def dashboard():
    # used to verify if user id is in sesssion already if not redirectr to homepage
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id' : session ["user_id"]
    }
    user = User.get_one_by_id(data)
    return render_template('/dashboard.html', user = user)

    # used to display the random recipe page
@app.route('/random_recipe')
def random_recipe():

    return render_template('random.html')

    # used to display the registration page and registration form for database use
@app.route('/register')
def register():
    return render_template('register.html')

    # used as action route to post form data to database with mysql query
@app.route('/save_user', methods=['POST'])
def save_user():
        # used to validate user if not rediredt to registration page
    if not User.validate_user(request.form):
        return redirect('/register')
        # used to hash password for data security
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        **request.form,
        "password": pw_hash
    }
    user_id = User.save_user(data)
        # used to save user in sesssion
    session['user_id'] = user_id
    User.save_user
    return redirect('/dashboard')

    #  used to display login page to user
@app.route('/login_page')
def login_page():
    return render_template('login.html')

    # used as action route to check if user is in database and validate password with bcrypt
@app.route('/login', methods=["POST"])
def login():
        # used to check if email is in database 
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/login_page")
        # used to check if password hash is correct
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/login_page')
        # saves user id in session
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

    # used as action route to clear session data 
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
