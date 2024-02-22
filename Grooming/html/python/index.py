from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from werkzeug.security import check_password_hash
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
    submit = SubmitField('Sign Up')

class DogDetailsForm(FlaskForm):
    dog_name = StringField('Dog Name', validators=[DataRequired()])
    breed = SelectField('Breed', choices=[('Affenpinscher', 'Affenpinscher'), ('Afghan Hound', 'Afghan Hound'), ('Africanis', 'Africanis'), ('Aidi', 'Aidi'), ('Airedale Terrier', 'Airedale Terrier'), ('Akbash', 'Akbash'), ('Akita', 'Akita'), ('Aksaray Malaklisi', 'Aksaray Malaklisi'), ('Alano Español', 'Alano Español'), ('Alapaha Blue Blood Bulldog', 'Alapaha Blue Blood Bulldog'), ('Alaskan husky', 'Alaskan husky'), ('Alaskan Klee Kai', 'Alaskan Klee Kai'), ('Alaskan Malamute', 'Alaskan Malamute'), ('Alopekis', 'Alopekis'), ('Alpine Dachsbracke', 'Alpine Dachsbracke'), ('American Bulldog', 'American Bulldog'), ('American Bully', 'American Bully'), ('American Cocker Spaniel', 'American Cocker Spaniel'), ('American English Coonhound', 'American English Coonhound'), ('American Eskimo Dog', 'American Eskimo Dog'), ('American Foxhound', 'American Foxhound'), ('American Hairless Terrier', 'American Hairless Terrier'), ('American Leopard Hound', 'American Leopard Hound'), ('American Pit Bull Terrier', 'American Pit Bull Terrier'), ('American Staffordshire Terrier', 'American Staffordshire Terrier'), ('American Water Spaniel', 'American Water Spaniel'), ('Anglo-Français de Petite Vénerie', 'Anglo-Français de Petite Vénerie'), ('Appenzeller Sennenhund', 'Appenzeller Sennenhund'), ('Ariège Pointer', 'Ariège Pointer'), ('Ariégeois', 'Ariégeois'), ('Argentine Pila', 'Argentine Pila'), ('Armant', 'Armant'), ('Armenian Gampr', 'Armenian Gampr'), ('Artois Hound', 'Artois Hound'), ('Assyrian Mastiff', 'Assyrian Mastiff'), ('Australian Cattle Dog', 'Australian Cattle Dog'), ('Australian Kelpie', 'Australian Kelpie'), ('Australian Shepherd', 'Australian Shepherd'), ('Australian Stumpy Tail Cattle Dog', 'Australian Stumpy Tail Cattle Dog'), ('Australian Terrier', 'Australian Terrier'), ('Austrian Black and Tan Hound', 'Austrian Black and Tan Hound'), ('Austrian Pinscher', 'Austrian Pinscher'), ('Australian Silky Terrier', 'Australian Silky Terrier'), ('Azawakh', 'Azawakh'), ('Bắc Hà', 'Bắc Hà'), ('Bakharwal', 'Bakharwal'), ('Bankhar Dog', 'Bankhar Dog'), ('Barak hound', 'Barak hound'), ('Barbado da Terceira', 'Barbado da Terceira'), ('Barbet', 'Barbet'), ('Basenji', 'Basenji'), ('Basque Shepherd Dog', 'Basque Shepherd Dog'), ('Basset Artésien Normand', 'Basset Artésien Normand'), ('Basset Bleu de Gascogne', 'Basset Bleu de Gascogne'), ('Basset Fauve de Bretagne', 'Basset Fauve de Bretagne'), ('Basset Hound', 'Basset Hound'), ('Bavarian Mountain Hound', 'Bavarian Mountain Hound'), ('Beagle', 'Beagle'), ('Beagle-Harrier', 'Beagle-Harrier'), ('Bearded Collie', 'Bearded Collie'), ('Beauceron', 'Beauceron'), ('Bedlington Terrier', 'Bedlington Terrier')])  # Add all breed options
    age = SelectField('Age', choices=[(str(i), str(i)) for i in range(1, 30)])  # Add all age options
    submit = SubmitField('Submit Dog Details')

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
    
INDEX_PAGE_PATH = '/Grooming/html/index.html'

@app.route(INDEX_PAGE_PATH)
def index():
    return render_template(INDEX_PAGE_PATH)

@app.route(INDEX_PAGE_PATH, methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate user credentials (customize this part based on your authentication mechanism)
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('static', filename='/Grooming/html/python/dashboard.html')) # Assuming you have a dashboard route
        else:
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for('index'))  # Redirect back to the login page

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup form submission
        form = SignupForm(request.form)

        if form.validate():
            # Retrieve user signup data
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # Check if the username or email is already taken
            existing_user = User.query.filter_by(username=username).first()
            existing_email = User.query.filter_by(email=email).first()

            if existing_user or existing_email:
                flash('Username or email already exists. Please choose different credentials.', 'error')
                return redirect(url_for('signup'))  # Redirect back to the signup page

            user_id = create_user(username, email, password)
            flash('Account created successfully!', 'success')
            login_user(User.query.get(user_id))
            return redirect(url_for('static', filename='/Grooming/html/python/dashboard.html')) # Assuming you have a dashboard route
        else:
            # Handle form validation errors
            flash('Error in form submission. Please check your inputs.', 'error')
            return redirect(url_for('index'))  # Redirect back to the signup page


