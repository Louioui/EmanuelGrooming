from curses import flash
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import os
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql://root:password@localhost/localhost')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secrets.token_hex(16)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    dogs = db.relationship('Dog', backref='owner', lazy=True)

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dog_name = db.Column(db.String(20), nullable=False)
    breed = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    dog_name = StringField('Dog Name', validators=[DataRequired()])
    breed = StringField('Breed', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_user(username, email, password):
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.id

def create_dog(user_id, dog_name, breed, age):
    new_dog = Dog(user_id=user_id, dog_name=dog_name, breed=breed, age=age)
    db.session.add(new_dog)
    db.session.commit()

@app.route('/')
def index():
    return render_template('/Grooming/html/index.html')

@app.route('/Grooming/php/process_signup.php', methods=['POST'])
def process_signup():
    form = SignupForm(request.form)

    if request.method == 'POST' and form.validate():
        # Retrieve user signup data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user_id = create_user(username, email, password)

        # Retrieve dog details
        dog_name = form.dog_name.data
        breed = form.breed.data
        age = form.age.data
        create_dog(user_id, dog_name, breed, age)

        return redirect(url_for('dashboard'))

    # Handle form validation errors (you can customize this part based on your needs)
    flash('Error in form submission. Please check your inputs.', 'error')
    return redirect(url_for('index'))

@app.route('/Grooming/html/dashboard.html')
@login_required
def dashboard():
    # Fetch and display user and dog details on the dashboard
    user = User.query.get(current_user.id)
    dogs = user.dogs
    return render_template('/Grooming/html/dashboard.html', user=user, dogs=dogs)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)







