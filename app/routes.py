from flask import render_template
from app import app

@app.route('/')#decorador: funcion que recibe otra funcion
@app.route('/index')
def index():
	user = {'username': 'Martha'}
	events = [
		{
			'name': 'WorkShop Python',
			'date': 'May 10'
		},
		{
			'name': 'Captura la Bandera',
			'date': 'May 10,11'
		}
	]
	return render_template('index.html', user = user,title = 'upslp', events = events)