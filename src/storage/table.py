import variables as Var
# import fileTracker.FileTracker as FileTracker
# import dataFile.DataFile as DataFile

from fileTracker import FileTracker as FileTracker
from dataFile import DataFile as DataFile
import fileUtility as FileUtility

import os
import json

class Table():
	def __init__(self,tableName,dbName):

		self.tableName=tableName
		self.dbName=dbName
		self.fileTrackerPath=Var.databaseStorageFilePath+self.dbName+"/"+self.tableName+"/fileTracker.json"
		self.dbPath=Var.databaseStorageFilePath+self.dbName+"/"
		self.tablePath=self.dbPath  + self.tableName + "/"
		self.primaryKey=""


	def _createTableDirectory( self ):
		if os.path.isdir(self.dbPath)==True:
			#todo: create directory
			tablePath=self.dbName+"/"+self.tableName
			tablePath=os.path.join(Var.databaseStorageFilePath,tablePath)
			os.mkdir(path = tablePath)
			#todo: create fileTracker
			fileTrackerPath=self.fileTrackerPath
			data=[]
			data.append({"keyStart":"-1","fileName":"data_0.json","writeCount":0,"entryCount":0})
			with open(fileTrackerPath,"w") as fp:
				json.dump(data,fp)

			#todo: create data files
			# tableDirectoryPath=self.tablePath
			for i in range( 0, Var.initialFileCountInTable ):
				filePath=self.tablePath+Var.dataFilePrefix+"_"+str(i)+".json"
				tableData=[]
				tableData.append({"primaryKey":"key","data":"null"})
				with open(filePath,"w") as f:
					json.dump(tableData,f)
		else:
			print("database does not exist! Table creation failed.")

	def createTable( self ):
		self._createTableDirectory()

	def setPrimaryKey( self,primaryKey ):
		self.primaryKey=primaryKey

	def insert( self, data, splittingPoint ):
		print ( "\n\n===================\n" )
		#todo: read fileTracker to find out which file to write to
		# step-1: handle the empty db case
		print("new data: ",data)
		fTracker=FileTracker(self.fileTrackerPath)
		fTrackerData=fTracker.getTrackerData()
		fileToInsert=""
		if fTrackerData[0]["keyStart"]=="-1":
			print("new DB")
			fTrackerData[0]["keyStart"]=data[self.primaryKey]
			fTrackerData[0]["writeCount"]=1
			fTrackerData[0]["entryCount"]=1
			fileToInsert=fTrackerData[0]["fileName"]


			fTracker.updateTrackerData ( fTrackerData )
			dataFile = DataFile ( self.tablePath + fileToInsert )
			tableData = dataFile.getTableData ( )
			if "primaryKey" in tableData [ 0 ] :
				# print("initial entry")
				tableData = [ ]
			tableData.append ( data )
			dataFile.updateTableData ( tableData )

		# step-2: handle already populated db case
		else:
			print("old DB")
			entryPlace={}
			counter=0
			for trackerData in fTrackerData:
				# print(trackerData["keyStart"]," --- ",data[self.primaryKey])
				if trackerData["keyStart"]<data[self.primaryKey]:
					entryPlace=trackerData
					counter += 1
				else:
					print("entered the break")
					break
			fileToInsert=entryPlace["fileName"]
			# entryPlace["writeCount"]=entryPlace["writeCount"]
			# entryPlace["entryCount"]=entryPlace["entryCount"]
			#todo: check if you need to split the file
			if entryPlace["entryCount"]+1>splittingPoint:
				print("needs split")
				#todo: if file split is needed,
					# 	i. create new fileTracker entries
					# ii. create new file and set it up for new entry

				currentInsertFileData=DataFile(self.tablePath+fileToInsert).getTableData()
				currentInsertFileData.append(data)

				part1 = currentInsertFileData [ :len ( currentInsertFileData ) // 2 ]
				part2=currentInsertFileData[len(currentInsertFileData)//2:]

				print ( "total length: ", len ( currentInsertFileData )," part1.length: ",len(part1),"part2.len: ",len(part2) )
				print("part1: ",part1)
				print("part2: ",part2)

				x=DataFile(self.tablePath+fileToInsert)
				x.updateTableData(part1)

				fTrackerData.pop(counter-1)
				entryPlace["writeCount"]=len(part1)
				entryPlace["entryCount"]=len(part1)
				fTrackerData.insert(counter-1,entryPlace)


				# print("new entry: keyStart: ",part2 [ 0 ] )
				newFileTrackerEntry = { "keyStart": part2 [ 0 ] [self.primaryKey ],
										"fileName": "data_"+FileUtility.generateRandomString (Var.datafileSuffixLength )+".json",
										"writeCount" : 0,
										"entryCount": len ( part2 )
										}

				newFilePath=self.tablePath+newFileTrackerEntry["fileName"]
				with open(newFilePath,"w") as json_file:
					dataToWrite=[]
					dataToWrite.append({"key":"null"})
					json.dump(dataToWrite,json_file)

				x=DataFile(newFilePath)
				x.updateTableData(part2)

				fTrackerData.insert ( counter, newFileTrackerEntry )
			else:
				print("does not need split")
				# print("fTrackerData:   ",fTrackerData)
				fTrackerData.pop ( counter - 1 )

				entryPlace["writeCount"]=entryPlace["writeCount"]+1
				entryPlace["entryCount"]=entryPlace["entryCount"]+1

				fTrackerData.insert(counter-1,entryPlace)
				print("fileToInsert: ",fileToInsert)
				dataFile = DataFile ( self.tablePath + fileToInsert )
				tableData = dataFile.getTableData ( )
				tableData.append ( data )

				dataFile.updateTableData ( tableData )


		#fixme: comment the next block out later
		#todo: update fileTracker if necessary
		fTracker.updateTrackerData (fTrackerData )
		#todo: write data to dataFile


		# dataFile = DataFile ( self.tablePath + fileToInsert )
		# tableData = dataFile.getTableData ( )
		# # case1: handle the initial dummy case
		# if "primaryKey" in tableData[0]:
		# 	# print("initial entry")
		# 	tableData=[]
		# # case2: handle the regular case
		# # print("tableData: ",tableData)
		# tableData.append(data)
		# # print("tableData: ",tableData)
		# dataFile.updateTableData(tableData)

		return

if __name__ == '__main__':
	os.system('rm -rf "/Users/sxs2561/Documents/OneDrive - The Pennsylvania State University/Course Work/cse_541/project/databases/db1/table1"')
	y=Table(tableName = "table1",dbName = "db1")
	y.createTable()
	y.setPrimaryKey(primaryKey ="nconst" )
	jsonFilePath="/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/inputs/name_basics.json"
	data=FileUtility.readJsonFile(jsonFilePath)
	splittingPoint=3
	for x in data:
		y.insert(x,splittingPoint)