import requests, json
from PronetDeviceApp.rest.domain.Container import Container
from PronetDeviceApp.rest.domain.Application import Application
from PronetDeviceApp.rest.domain.ContentInstance import ContentInstance 
from PronetDeviceApp.utils.constants import *

class DeviceSimulator():
	_appId = False
	_isCreated = False
	_m2mPoC = False
	_deviceId = False

	def init(self, appId, m2mPoC):
		self._appId = appId
		self._m2mPoC = m2mPoC
		self._isCreated = True
		self._deviceId = False

	def isCreated(self):
		return self._isCreated

	def getAppId(self):
		return self._appId

	def getm2mPoC(self):
		return self._m2mPoC

	def getDeviceId(self):
		return self._deviceId

	@classmethod
	def autoConfigure(cls, m2mPoC, aPoC, aPoCPaths):
		jsonBody = Application(obj_dict={'aPoC':aPoC, 
								'searchStrings': APP_SEARCH_STRING_LIST, 
								'accessRightID': APP_ACCESS_RIGHTS_ID,
								'aPoCPaths': aPoCPaths}).toJson()
		commandUrl = m2mPoC + "/pronet/applications"
		headers={'content-type': 'application/json'}
		try:
			restResp = requests.post(commandUrl, data=jsonBody, headers=headers)
			respdict = json.loads(restResp.content)
		except Exception as e:
			raise Exception(e, commandUrl, jsonBody, restResp.content)
		netApp = cls()
		netApp.init(respdict['appId'], m2mPoC)
		return netApp

	def sendDeviceParams(self):
		contentInstance = ContentInstance()
		contentInstance.setContent("SIMULATOR CONTENT")
		contentUrl = self._m2mPoC + "/pronet/applications/" + \
					 self._appId + "/containers/" + self._deviceId + "/contentinstances"
		headers={'content-type': 'application/json'}
		
		try:
			restResp = requests.post(contentUrl, data=contentInstance.toJson(), headers=headers)
			respdict = json.loads(restResp.content)
		except Exception as e:
			raise Exception(e, contentUrl, contentInstance.toJson(), restResp.content)
		contentResp = ContentInstance(json.loads(restResp.content))
		return contentResp

	def createDevice(self):
		device = Container()
		commandUrl = self._m2mPoC + "/pronet/applications/" + \
					 self._appId + "/containers"
		headers={'content-type': 'application/json'}
		try:
			restResp = requests.post(commandUrl, data=device.toJson(), headers=headers)
			respdict = json.loads(restResp.content)
		except Exception as e:
			raise Exception(e, commandUrl, device.toJson(), restResp.content)
		print respdict
		newDevice = Container(respdict)
		self._deviceId = newDevice.getContainerId()
		return newDevice

