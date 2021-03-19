import json
class FileTracker():
	def __init__(self,fileTrackerPath):
		self.fileTrackerPath=fileTrackerPath
		with open(self.fileTrackerPath,"r") as json_file:
			self.trackerData=json.load(json_file)

	def getTrackerData( self ):
		return self.trackerData

	def updateTrackerData( self,trackerData ):
		self.trackerData=trackerData
		with open(self.fileTrackerPath,"w") as json_file:
			json.dump(self.trackerData,json_file)



if __name__ == '__main__':
	x=FileTracker(fileTrackerPath = "/Users/sxs2561/Documents/OneDrive - The Pennsylvania State University/Course Work/cse_541/project/databases/db1/table1/fileTracker.json")
	for y in x.getTrackerData():
		print(y)
