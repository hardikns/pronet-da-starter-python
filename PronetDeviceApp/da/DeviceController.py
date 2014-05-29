from flask import Flask, request
from flask.ext.restful import Resource, reqparse
from PronetDeviceApp.da.core.CommandInfo import CommandInfo 
from PronetDeviceApp.da.core.DeviceSimulator import DeviceSimulator
import httplib
import json

class DeviceController():
	_api = False
	_parser = False
	_deviceSimulator = False

	class Configure(Resource):
		def get(self):
			parser = reqparse.RequestParser()
			parser.add_argument('m2mPoC', type=str, required=True, location='args')
			parser.add_argument('appId', type=str, required=True, location='args')
			args = parser.parse_args()
			m2mPoC = args.get('m2mPoC', False)
			appId = args.get('appId', False)
			if not DeviceController._deviceSimulator or DeviceController._deviceSimulator.isCreated() == False:
				DeviceController._deviceSimulator = DeviceSimulator()
				DeviceController._deviceSimulator.init(appId, m2mPoC)
				return "Device Simulator Configured Successfully", httplib.OK
			else:
				return "DA Reconfiguration Forbidden", httplib.FORBIDDEN

	class AutoConfigure(Resource):
		def get(self):
			parser = reqparse.RequestParser()
			parser.add_argument('m2mPoC', type=str, required=True, location='args')
			parser.add_argument('aPoCPath', type=str, required=True, location='args')
			args = parser.parse_args()
			m2mPoC = args.get('m2mPoC', False)
			aPoCPath = args.get('aPoCPath', False)
			aPoCPaths = [aPoCPath]
			aPoC = request.url_root


			if not DeviceController._deviceSimulator:
				try: 
					DeviceController._deviceSimulator = DeviceSimulator.autoConfigure(m2mPoC, aPoC, aPoCPaths)
				except Exception as e:
					return """Communication with Pronet failed<br>Request<br>%s<br>json:%s<br>
					          Error Received from Pronet%s""" % (e[1], e[2], e[3]), httplib.FORBIDDEN
				else:
					return "Device Simulator Configured with Pronet at " + m2mPoC + \
							" appId " +  DeviceController._deviceSimulator.getAppId(), httplib.OK
			else:
				return "Already Configured with " + DeviceController._deviceSimulator.getm2mPoC() + \
						" appId " +  DeviceController._deviceSimulator.getAppId(), httplib.FORBIDDEN

	class CreateDevice(Resource):
		def get(self):
			deviceSimulator = DeviceController._deviceSimulator 
			if deviceSimulator and deviceSimulator.getDeviceId() == False:
				try:
					device = deviceSimulator.createDevice()
				except Exception as e:
					return """CreateDevice Failed<br>Request<br>%s<br>json:%s<br>
					          Error Received from Pronet%s""" % (e[1], e[2], e[3]), httplib.FORBIDDEN
				deviceId = device.getContainerId()
				print "Device Id :" + deviceId
				return "Device Created Successfully, Device Id :" + deviceId, httplib.OK
			elif not deviceSimulator:
				return "Add Device Forbidden, Configure Device Simulator", httplib.FORBIDDEN
			else:
				return "Device Exists , Device Id: " + deviceSimulator.getDeviceId(), httplib.FORBIDDEN

	class SendDeviceParams(Resource):
		def get(self):
			deviceSimulator = DeviceController._deviceSimulator 
			if deviceSimulator and deviceSimulator.getDeviceId() != False:
				try:
					deviceParm = deviceSimulator.sendDeviceParams()
				except Exception as e:
					return """CreateDevice Failed<br>Request<br>%s<br>json:%s<br>
					          Error Received from Pronet%s""" % (e[1], e[2], e[3]), httplib.FORBIDDEN

				resp_string = "Device Id: " + deviceSimulator.getDeviceId() + \
					" Reading Reference: " + deviceParm.getContentInstanceId()
				print resp_string
				return  resp_string, httplib.OK
			elif not deviceSimulator:
				return "Add Device Forbidden, Configure Device Simulator", httplib.FORBIDDEN
			else:
				return "No Device Exists", httplib.FORBIDDEN


	class ReceiveCommand(Resource):
		def post(self, appId, deviceId):

			deviceSimulator = DeviceController._deviceSimulator 

			try: 
				command_dict = json.loads(request.content)
				command = CommandInfo(appId, deviceId, command_dict)
			except Exception as e:
				return "Exception:%s<br>In Valid Command Received%s" % (e, request.content), \
						httplib.FORBIDDEN  
			return "Success Guaranteed", httplib.OK

				 

	def __init__(self, api):
		_api = api
		api.add_resource(self.Configure,'/pronet-da-starter/configure')
		api.add_resource(self.AutoConfigure, '/pronet-da-starter/autoconfigure')
		api.add_resource(self.CreateDevice, '/pronet-da-starter/create-device')
		api.add_resource(self.SendDeviceParams, 
			"/pronet-da-starter/send-device-params")
		api.add_resource(self.ReceiveCommand, 
			'/pronet-da-starter/applications/<string:appId>/containers/<string:deviceId>/commands')

			




