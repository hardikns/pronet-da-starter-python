from PronetDeviceApp.utils.datetime_new import datetime
import json

class ContentInstance():
	contentInstanceId = False       # String
	creationTime = None             # Datetime (converted from Epoch format)
	lastModifiedTime = None			# Datetime (converted from Epoch format)
	contentTypes = []				# List of String
	mimeType = []					# List of String
	contentSize = 0					# int
	content = False					# String

	def toJson(self):
		obj_dict = self.__dict__
		obj_dict['creationTime'] = obj_dict['creationTime'] and \
		                           obj_dict['creationTime'].epoch() or 0
		obj_dict['lastModifiedTime'] = obj_dict['lastModifiedTime'] and \
									   obj_dict['lastModifiedTime'].epoch() or 0
		return json.dumps(obj_dict)

	def __init__(self, obj_dict=None):
		self.contentInstanceId = False       
		self.creationTime = None             
		self.lastModifiedTime = None		
		self.contentTypes = []				
		self.mimeType = []					
		self.contentSize = 0					
		self.content = False					
		if obj_dict == None:
			return
		for key in self.__dict__.keys():
			self.__dict__[key] = obj_dict.get(key, None)
		if isinstance(self.creationTime, (int, long)): 
			self.creationTime = datetime.fromEpoch(self.creationTime)
		if isinstance(self.lastModifiedTime, (int, long)): 
			self.lastModifiedTime = datetime.fromEpoch(self.lastModifiedTime)

	def getContentInstanceId(self):
		return self.contentInstanceId

	def getCreationTime(self):
		return self.creationTime

	def getLastModifiedTime(self):
		return self.lastModifiedTime

	def getContentTypes(self):
		return self.contentTypes

	def getMimeType(self):
		return self.mimeType

	def getContentSize(self):
		return self.contentSize

	def getContent(self):
		return self.content

	def setContentInstanceId(self, contentInstanceId):
		self.contentInstanceId = contentInstanceId

	def setCreationTime(self, creationTime):
		self.creationTime = creationTime

	def setLastModifiedTime(self, lastModifiedTime):
		self.lastModifiedTime = lastModifiedTime

	def setContentTypes(self, contentTypes):
		self.contentTypes = contentTypes

	def setMimeType(self, mimeType):
		self.mimeType = mimeType

	def setContentSize(self, contentSize):
		self.contentSize = contentSize

	def setContent(self, content):
		self.content = content