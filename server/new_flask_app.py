
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from email.policy import default
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import Flask, jsonify
import json
import datetime as dt
from firebase_admin import credentials, firestore, initialize_app
import uuid
import bcrypt
# Initialize Flask App

from datetime import datetime
import json
import numpy as np
import os
#import cv2
# import send_file
from flask_cors import CORS
print(os.getcwd())

app = Flask(__name__)
CORS(app)


# Initialize Firestore DB
pyawr = os.getcwd() + '/mysite/'
cred = credentials.Certificate(
    pyawr + 'blogsugeeth-firebase-adminsdk-mcte0-50e1c6497f.json')
default_app = initialize_app(cred)
db = firestore.client()

user = db.collection('Users')

'''Basic Premise of the App
USers can sign up and login
Users have basic deatils, like name, email, password, joining date, last login date, etc.
Users have list of blogs they need to do and their status which are sorted by date
'''

# APIs

# Register
# Login
# Create blog
# Edit blog
# Delete blog
# Get blog
# Get all blogs

# Blog schema

# Id
# Title
# Hero image
# Content
# Created at


def send_response(status, message, data=None):
    # convert all values to string
    if data is not None:
        # print(data)
        if 'password' in data.keys():
            del data['password']
        for key in data:
            if isinstance(data[key], datetime):
                data[key] = data[key].isoformat()
            if isinstance(data[key], np.ndarray):
                data[key] = data[key].tolist()
            if isinstance(data[key], np.int64):
                data[key] = int(data[key])
        if 'blogs' in data.keys():
            Blogs = []
            for blog in data['blogs']:
                blog['id'] = str(blog['id'])
                blog['date'] = str(blog['date'])
                # save blog in data
                Blogs.append(blog)
            # print(Blogs)
            data['blogs'] = Blogs
        # print('******************')
        print(data)
        data = json.dumps(data)
        print(data)
    response = jsonify({
        'status': status,
        'message': message,
        'data': data
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def validate_password(password):
    if len(password) < 8:
        return send_response(400, 'Password must be at least 8 characters long')
    elif password.isdigit():
        return send_response(400, 'Password must contain at least one letter')
    elif password.isalpha():
        return send_response(400, 'Password must contain at least one number')
    elif password.islower():
        return send_response(400, 'Password must contain at least one uppercase letter')
    elif password.isupper():
        return send_response(400, 'Password must contain at least one lowercase letter')
    elif password.count(' ') > 0:
        return send_response(400, 'Password must not contain any spaces')
    elif password.count('!') > 0:
        return send_response(400, 'Password must not contain any exclamation marks')
    else:
        return True


def UsernameExists(Uname):
    try:
        if user.document(Uname).get().exists == True:
            return True
    except Exception as e:
        return send_response(400, 'Username already Taken')


@app.route('/Register', methods=['POST'])
def Register():
    if request.method == 'POST':
        print(request.data)
        data = json.loads(request.data)
        print(data)
        if UsernameExists(data['username']):
            return send_response(400, 'Username already taken')
        validate_passwordR = validate_password(data['password'])
        if validate_passwordR != True:
            return validate_passwordR
        else:
            data['password'] = bcrypt.hashpw(
                data['password'].encode('utf-8'), bcrypt.gensalt())
            data['joining_date'] = datetime.now()
            data['last_login_date'] = datetime.now()
            data['blogs'] = []
            user.document(data['username']).set(data)
            return send_response(200, 'User Registered Successfully')
    else:
        return send_response(500, 'Incorrect Request method')


@app.route('/Login', methods=['POST'])
def Login():
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data)
        if UsernameExists(data['username']):
            user_data = user.document(data['username']).get().to_dict()
            if bcrypt.checkpw(data['password'].encode('utf-8'), user_data['password']):
                user_data['last_login_date'] = datetime.now()
                user.document(data['username']).set(user_data)
                return send_response(200, 'User Logged in Successfully')
            else:
                return send_response(400, 'Invalid Password')
        else:
            return send_response(400, 'Invalid Username')
    else:
        return send_response(500, 'Incorrect Request method')


@app.route('/GetUser', methods=['GET'])
def GetUser():
    if request.method == 'GET':
        data = request.args
        print(data)
        data = dict(data)
        if UsernameExists(data['username']):
            user_data = user.document(data['username']).get().to_dict()
            return send_response(200, 'User Data', user_data)
        else:
            return send_response(400, 'Invalid Username')
    else:
        return send_response(500, 'Incorrect Request method')


def createBlog(data):
    data['date'] = datetime.now().strftime("%d %b %Y")
    if 'id' not in data.keys():
        data['id'] = str(uuid.uuid4())
    return data


@app.route('/AddBlog', methods=['POST'])
def AddBlog():
    if request.method == 'POST':
        data = json.loads(request.data)
        if UsernameExists(data['username']):
            user_data = user.document(data['username']).get().to_dict()
            user_data['blogs'].append(createBlog(data))
            user.document(data['username']).set(user_data)
            return send_response(200, 'Blog Added Successfully', data)
        else:
            return send_response(400, 'Invalid Username')
    else:
        return send_response(500, 'Incorrect Request method')


@app.route('/GetBlogs', methods=['POST'])
def GetBlogs():
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data)
        # data = dict(data)
        if UsernameExists(data['username']):
            user_data = user.document(data['username']).get().to_dict()
            return send_response(200, 'Blogs Fetched Successfully', user_data)
        else:
            return send_response(400, 'Invalid Username')
    else:
        return send_response(500, 'Incorrect Request method')


@app.route('/UpdateBlog', methods=['POST'])
def UpdateBlog():
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data)
        if UsernameExists(data['username']):
            user_data = user.document(data['username']).get().to_dict()
            for blog in user_data['blogs']:
                if str(blog['id']) == data['id']:
                    user_data['blogs'].remove(blog)
                    user_data['blogs'].append(createBlog(data))
                    user.document(data['username']).set(user_data)
                    return send_response(200, 'Blog Updated Successfully')
            return send_response(400, 'Invalid Blog ID')
        else:
            return send_response(400, 'Invalid Username')
    else:
        return send_response(500, 'Incorrect Request method')


@app.route('/DeleteBlog', methods=['POST'])
def DeleteBlog():
    if request.method == 'POST':
        data = json.loads(request.data)
        if UsernameExists(data['username']):
            user_data = user.document(data['username']).get().to_dict()
            for blog in user_data['blogs']:
                if blog['id'] == data['id']:
                    user_data['blogs'].remove(blog)
                    user.document(data['username']).set(user_data)
                    return send_response(200, 'Blog Deleted Successfully')
            return send_response(400, 'Invalid Blog ID')
        else:
            return send_response(400, 'Invalid Username')
    else:
        return send_response(500, 'Incorrect Request method')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='


@app.route('/')
def hello_world():
    return 'Hello from Flask!'
