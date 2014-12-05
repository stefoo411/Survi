from flask import Flask, render_template, request, redirect
import jinja2
import os
from pymongo import *
import os

app = Flask(__name__)

app.secret_key = 'kbwkfwbhwbhk'
client = MongoClient('mongodb://survistefoo:survi@ds051110.mongolab.com:51110/survi')
db = client.get_default_database()
users = db.users

@app.route('/')
def hello():
	#users.insert({'username':'paras2','password':'cool'})
	return render_template("index.html")

@app.route('/change')
def chance():
	return redirect('/')

@app.route('/post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		return render_template('post.html')
	return render_template('get.html')

@app.route('/login', methods=['GET','POST'])
def login():
	users = db.users
	users = users.find({})
	return render_template('get.html',users=users)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)
