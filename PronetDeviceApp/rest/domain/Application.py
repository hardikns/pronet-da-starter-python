from PronetDeviceApp.utils.datetime_new import datetime
import json

class Application():
	appId = None                         # String
	accessRightID = None                 # String               
	searchStrings = []                   # List of Strings
	creationTime = None                  # Datetime (converted from Epoch format)
	lastModifiedTime = None              # Datetime (converted from Epoch format)
	aPoC = None                          # String
	aPoCPaths = []                       # List of Strings
	containersReference = None           # String
	groupsReference = None               # String 
	accessRightsReference = None         # String
	notificationChannelReference = None  # String

	def __init__(self, obj_dict=None):
		self.appId = None                         
		self.accessRightID = None                                
		self.searchStrings = []                   
		self.creationTime = None                  
		self.lastModifiedTime = None              
		self.aPoC = None                          
		self.aPoCPaths = []                       
		self.containersReference = None           
		self.groupsReference = None                
		self.accessRightsReference = None         
		self.notificationChannelReference = None  
		if obj_dict == None:
			return
		for key in self.__dict__.keys():
			self.__dict__[key] = obj_dict.get(key, None)
		if isinstance(self.creationTime, (int, long)): 
			self.creationTime = datetime.fromEpoch(self.creationTime)
		if isinstance(self.lastModifiedTime, (int, long)): 
			self.lastModifiedTime = datetime.fromEpoch(self.lastModifiedTime)

	def toJson(self):
		obj_dict = self.__dict__
		obj_dict['creationTime'] = obj_dict['creationTime'] and \
		                           obj_dict['creationTime'].epoch() or 0
		obj_dict['lastModifiedTime'] = obj_dict['lastModifiedTime'] and \
									   obj_dict['lastModifiedTime'].epoch() or 0
		return json.dumps(obj_dict)

	def getAppId(self):
	    return self.appId

	def getAccessRightID(self):
	    return self.accessRightID

	def getSearchStrings(self):
	    return self.searchStrings

	def getCreationTime(self):
	    return self.creationTime

	def getLastModifiedTime(self):
	    return self.lastModifiedTime

	def getAPoC(self):
	    return self.aPoC

	def getAPoCPaths(self):
	    return self.aPoCPaths

	def getContainersReference(self):
	    return self.containersReference

	def getGroupsReference(self):
	    return self.groupsReference

	def getAccessRightsReference(self):
	    return self.accessRightsReference

	def getNotificationChannelReference(self):
	    return self.notificationChannelReference

	def setAppId(self, appId):
	    self.appId = appId

	def setAccessRightID(self, accessRightID):
	    self.accessRightID = accessRightID

	def setSearchStrings(self, searchStrings):
	    self.searchStrings = searchStrings

	def setCreationTime(self, creationTime):
	    self.creationTime = creationTime

	def setLastModifiedTime(self, lastModifiedTime):
	    self.lastModifiedTime = lastModifiedTime

	def setAPoC(self, aPoC):
	    self.aPoC = aPoC

	def setAPoCPaths(self, aPocPaths):
	    self.aPoCPaths = aPocPaths

	def setContainersReference(self, containersReference):
	    self.containersReference = containersReference

	def setGroupsReference(self, groupsReference):
	    self.groupsReference = groupsReference

	def setAccessRightsReference(self, accessRightsReference):
	    self.accessRightsReference = accessRightsReference

	def setNotificationChannelReference(self, notificationChannelReference):
	    self.notificationChannelReference = notificationChannelReference