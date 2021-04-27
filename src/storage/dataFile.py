import json
import src.storage.fileUtility as FileUtility
class DataFile():
	def __init__(self,dataFilePath):
		self.dataFilePath=dataFilePath
		with open(self.dataFilePath,"r") as json_file:
			self.data=json.load(json_file)

	def getTableData( self ):
		return self.data

	def updateTableData( self,data ):
		self.data=data
		# print("self.data: ",self.data)
		with open(self.dataFilePath,"w") as json_file:
			json.dump(self.data,json_file)
		# FileUtility.atomicWriteToFile(filePath = self.dataFilePath,data = self.data)
		return

