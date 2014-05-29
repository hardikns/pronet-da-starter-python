from PronetDeviceApp.utils.datetime_new import datetime
import json

class Command():
	commandId = None	              # String
	creationTime = None               # Datetime (converted from Epoch format)
	lastModifiedTime = None           # Datetime (converted from Epoch format)
	commandType = None                # String
	execEnable = None                 # bool
	description = None                # String
	execInstancesReference = None     # String
	subscriptionsReference = None     # String
	command = None                    # int

	def toJson(self):
		obj_dict = self.__dict__
		obj_dict['creationTime'] = obj_dict['creationTime'] and \
		                           obj_dict['creationTime'].epoch() or 0
		obj_dict['lastModifiedTime'] = obj_dict['lastModifiedTime'] and \
									   obj_dict['lastModifiedTime'].epoch() or 0
		return json.dumps(obj_dict)

	def __init__(self, obj_dict=None):
		self.commandId = None	              
		self.creationTime = None               
		self.lastModifiedTime = None           
		self.commandType = None                
		self.execEnable = None                 
		self.description = None                
		self.execInstancesReference = None     
		self.subscriptionsReference = None     
		self.command = None                    
		if obj_dict == None:
			return
		for key in self.__dict__.keys():
			self.__dict__[key] = obj_dict.get(key, None)
		if isinstance(self.creationTime, (int, long)): 
			self.creationTime = datetime.fromEpoch(self.creationTime)
		if isinstance(self.lastModifiedTime, (int, long)): 
			self.lastModifiedTime = datetime.fromEpoch(self.lastModifiedTime)

	def getCommandId(self):
		return self.commandId

	def setCommandId(self, commandId):
		self.commandId = commandId

	def getCreationTime(self):
		return self.creationTime

	def setCreationTime(self, creationTime):
		self.creationTime = creationTime

	def getLastModifiedTime(self):
		return self.lastModifiedTime

	def setLastModifiedTime(self, lastModifiedTime):
		self.lastModifiedTime = lastModifiedTime

	def getCommandType(self):
		return self.commandType

	def setCommandType(self, commandType):
		self.commandType = commandType

	def getExecEnable(self):
		return self.execEnable

	def setExecEnable(self, execEnable):
		self.execEnable = execEnable

	def getDescription(self):
		return self.description

	def setDescription(self, description):
		self.description = description

	def getExecInstancesReference(self):
		return self.execInstancesReference

	def setExecInstancesReference(self, execInstancesReference):
		self.execInstancesReference = execInstancesReference

	def getSubscriptionsReference(self):
		return self.subscriptionsReference

	def setSubscriptionsReference(self, subscriptionsReference):
		self.subscriptionsReference = subscriptionsReference

	def getCommand(self):
		return self.command

	def setCommand(self, command):
		self.command = command
