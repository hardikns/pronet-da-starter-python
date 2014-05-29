from flask import Flask
from flask.ext.restful import Api
from DeviceController import DeviceController

def main(host, port):
	app = Flask(__name__)
	api = Api(app)
	dc = DeviceController(api)
	app.run(debug=True, host=host, port=port )
