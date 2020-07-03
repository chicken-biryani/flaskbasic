from flask import Flask
app=Flask(__name__)

@app.route('/')
@app.route('/home') 
'''the url http://127.0.0.1:5000/ and http://127.0.0.1:5000/home
will have the same return'''
def hello():
	return <h1>HELLO THERE</h1>

@app.route('/about')
def about():
	return <h1>ABOUT</h1>