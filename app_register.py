from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for flash messages

# MongoDB setup
client = MongoClient("mongodb+srv://2407312:5telaTh3G0at@Cluster0.y0xio.mongodb.net/login")
db = client['login']  # Replace with your database name
users_collection = db['login']  # Replace with your collection name

# Home route
@app.route('/')
def home():
    return render_template('registerpage.html')  # Home page with link to register page

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Input validation
        if not username or not email or not password or not confirm_password:
            flash('All fields are required.', 'error')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('register'))

        # Password validation (length check)
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
            return redirect(url_for('register'))

        # Email validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            flash('Invalid email format.', 'error')
            return redirect(url_for('register'))

        # Check if the username or email already exists in the database
        existing_user = users_collection.find_one({"username": username})
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))

        existing_email = users_collection.find_one({"email": email})
        if existing_email:
            flash('Email already registered. Please use a different email.', 'error')
            return redirect(url_for('register'))

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Insert the new user into the database
        users_collection.insert_one({
            "username": username,
            "email": email,
            "password": hashed_password
        })

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('home'))

    return render_template('registerpage.html')  # Render the registration page

if __name__ == '__main__':
    app.run(debug=True)
