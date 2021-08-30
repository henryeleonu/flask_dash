# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from dash_app.multi import create_multi_app
from flask import Flask
from dash_app.graph import create_dash_application
from dash_app.chart import create_chart_app
#from dash_app import create_multi_app

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
create_dash_application(app)
create_chart_app(app)
create_multi_app(app)
#dashboard.get_asset_url('/dash/')
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello World'


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
