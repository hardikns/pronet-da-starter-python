from PronetDeviceApp.rest.domain.Command import Command 
from datetime import datetime

class CommandInfo():
	_command = False
	_appId = False
	_deviceId = False
	_receivedTime = False

	def __init__(self, appId, deviceId, command_dict):
	
		self._command = Command(command_dict)
		self._appId = appId
		self._deviceId = deviceId
		self._receivedTime = datetime.now()

	def getCommand(self):
		return self._contentInstance

	def getAppId(self):
		return self._appId

	def getDeviceId(self):
		return self._deviceId

	def getReceivedTime(self):
		return self._receivedTime

	def __str__(self):
		return """
		Device Command Received.......
		Command          : %s 
		App Id           : %s 
		Device Id        : %s  
		Time of Issue    : %s 
		Recieved Time    : %s 
		-----------------------------""" %  (	self._command.getCommand(),
											 	self._appId,
											 	self._deviceId,
											 	self._command.getCreationTime(),
											 	self._receivedTime) 


