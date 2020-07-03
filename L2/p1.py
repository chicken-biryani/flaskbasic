from flask import Flask,render_template
app=Flask(__name__)

posts=[
{
	'author':'Corey',
	'title':'Blog post 1',
	'content':'first blog post',
	'date_posted':'june 12'
},
{
	'author':'Jane',
	'title':'Blog post 2',
	'content':'second blog post',
	'date_posted':'june 13'
}




]

@app.route('/')
@app.route('/home')
def hello():
	return render_template('home.html',posts=posts)

@app.route('/about')
def about():
	return render_template('about.html',title='about')