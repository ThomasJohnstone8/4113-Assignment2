from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to MongoDB
client = MongoClient("mongodb+srv://2407312:5telaTh3G0at@Cluster0.y0xio.mongodb.net/login")
db = client['login']
users_collection = db['login']

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route('/')
def registerpage():
    return render_template('registerpage.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = users_collection.find_one({'email': email})

    if user and check_password_hash(user['password'], password):
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Invalid credentials. Please try again.', 'error')
        return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        existing_user = users_collection.find_one({'email': email})

        if existing_user:
            flash('Email already exists! Please use a different email.', 'error')
            return redirect('/register')

        password = request.form['password']
        hashed_password = generate_password_hash(password)
        users_collection.insert_one({'email': email, 'password': hashed_password})

        flash('Registration successful! Please log in.', 'success')
        return redirect('home.html')
    
    # Render template without flashing messages on GET request
    return render_template('registerpage.html')


if __name__ == '__main__':
    app.run(debug=True)