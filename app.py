from flask import Flask, request, render_template, redirect, url_for
from config import Config
from operations import Operations
app = Flask(__name__)
app.config['SECRET_KEY']='tempconfig'

"""The application is a basic calculator that has a single server route called index. The input from the user is handled through a python Flask form with the backend processing done through python. All files associated with the UI are within the templates directory. To run the application locally, the main file can be exported as app.py (export FLASK_APP="app.py" and then invoked through the command: flask run"""

@app.route('/', methods=['GET', 'POST'])
def index():	
	form = Operations()
	output = 0
	if form.validate_on_submit():
		one = int(request.form['one'])
		two = int(request.form['two'])	
		output = one+two if request.form['button'] == "+" else one-two if request.form['button'] == "-" else one*two if request.form['button'] == "X" else one/two if request.form['button'] == "/" else 0
		
		if request.form['button'] == "Clear":
			return redirect(url_for('index'))
	
	return render_template("operations.html", output=output, form=form)
	
