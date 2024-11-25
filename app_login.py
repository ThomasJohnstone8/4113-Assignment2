from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb+srv://2407312:5telaTh3G0at@Cluster0.y0xio.mongodb.net/toolsDB")
db = client.toolsDB
tools_collection = db.tools
comments_collection = db.comments

@app.route('/mainpage.html')
def home()
    if session['username'] = username
    return render_template('/homelogin.html')
else
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST"
    email = request.form['email']
    exisiting_user = user_collection.find_one[{'email': email}]

    if existing_user:
        flash('Email is already taken, try again.')
        return redirect('/registerpage.html')

        password = request.form['password']
        hashed_password = generate_password_hash(password)
        users_collection.insert_one({'email': email})

        flash('Registration successful! Please log in', 'success')
        return redirect('/login.html')

    return render_template('/registerpage.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if user and check_password_hash(user['password'], pasword):
        flash('Login successful!', 'success')
        return redirect('/homelogin.html')
    else
        flash('invalid username or password, try again.', 'error')
        return redirect('/login.html')
    
















