from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use your actual database URI
db = SQLAlchemy(app)

class User(db.Model):
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

@app.route('/')
def index():
    return render_template('/Grooming/html/index.html')

@app.route('/Grooming/php/process_signup.php', methods=['POST'])
def process_signup():
    if request.method == 'POST':
        # Retrieve user signup data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Store user details in the database
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Retrieve dog details
        dog_name = request.form.get('dog_name')
        breed = request.form.get('breed')
        age = request.form.get('age')

        # Get the user ID of the newly registered user
        user_id = new_user.id

        # Store dog details in the database
        new_dog = Dog(dog_name=dog_name, breed=breed, age=age, user_id=user_id)
        db.session.add(new_dog)
        db.session.commit()

        return "<script>window.location.href='/Grooming/html/dashboard.html';</script>"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)



