import json
import src.storage.fileUtility as FileUtility

class FileTracker():
	def __init__(self,fileTrackerPath):
		self.fileTrackerPath=fileTrackerPath
		with open(self.fileTrackerPath,"r") as json_file:
			self.trackerData=json.load(json_file)

	def getTrackerData( self ):
		return self.trackerData

	def updateTrackerData( self,trackerData ):
		self.trackerData=trackerData
		# with open(self.fileTrackerPath,"w") as json_file:
		# 	json.dump(self.trackerData,json_file)
		FileUtility.atomicWriteToFile(filePath = self.fileTrackerPath,data = self.trackerData)




if __name__ == '__main__':
	x=FileTracker(fileTrackerPath = "/Users/rxh655/Documents/Spring\ 2021/CSE\ 541/Project/imdb_kaggle_small/title_principals/fileTracker.json ")
	for y in x.getTrackerData():
		print(y)
