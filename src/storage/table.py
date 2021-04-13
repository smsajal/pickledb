# import variables as Var
import src.storage.variables as Var

from src.storage.fileTracker import FileTracker as FileTracker
from src.storage.dataFile import DataFile as DataFile
import src.storage.fileUtility as FileUtility
from src.storage.database import Database as Database
from src.storage.tempResult import TempResult as TempResult

import os
import json
import sys

class Table():
	def __init__(self,tableName,dbName, primaryKey=""):

		self.tableName=tableName
		self.dbName=dbName
		self.fileTrackerPath=Var.databaseStorageFilePath+self.dbName+"/"+self.tableName+"/fileTracker.json"
		self.dbPath=Var.databaseStorageFilePath+self.dbName+"/"
		self.tablePath=self.dbPath  + self.tableName + "/"
		self.primaryKey=primaryKey



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
			# with open(fileTrackerPath,"w") as fp:
			# 	json.dump(data,fp)
			FileUtility.atomicWriteToFile(filePath = fileTrackerPath,data = data)

			#todo: create data files
			# tableDirectoryPath=self.tablePath
			for i in range( 0, Var.initialFileCountInTable ):
				filePath=self.tablePath+Var.dataFilePrefix+"_"+str(i)+".json"
				tableData=[]
				tableData.append({"primaryKey":"key","data":"null"})
				# with open(filePath,"w") as f:
				# 	json.dump(tableData,f)
				FileUtility.atomicWriteToFile(filePath = filePath,data = tableData)
		else:
			print("database does not exist! Table creation failed.")

	def createTable( self ):
		self._createTableDirectory()

	def setPrimaryKey( self,primaryKey ):
		self.primaryKey=primaryKey


	def getPrimaryKey ( self ) :
		return self.primaryKey

	def insert( self, data, splittingPoint ):

		'''
			args:
				data: json object of data
				splittingPoint: max number of entries in datafile after which the datafile has to split
		'''

		#todo: read fileTracker to find out which file to write to
		# step-1: handle the empty db case

		fTracker=FileTracker(self.fileTrackerPath)
		fTrackerData=fTracker.getTrackerData()
		fileToInsert=""


		if fTrackerData[0]["keyStart"]=="-1":

			fTrackerData[0]["keyStart"]=data[self.primaryKey]
			fTrackerData[0]["writeCount"]=1
			fTrackerData[0]["entryCount"]=1
			fileToInsert=fTrackerData[0]["fileName"]


			fTracker.updateTrackerData ( fTrackerData )
			dataFile = DataFile ( self.tablePath + fileToInsert )
			tableData = dataFile.getTableData ( )
			if "primaryKey" in tableData [ 0 ] :
				tableData = [ ]
			tableData.append ( data )
			dataFile.updateTableData ( tableData )

		# step-2: handle already populated db case
		else:

			entryPlace={}
			counter=0
			for trackerData in fTrackerData:
				if trackerData["keyStart"]<data[self.primaryKey]:
					entryPlace=trackerData
					counter += 1
				else:
					break

			fileToInsert=entryPlace["fileName"]
			# entryPlace["writeCount"]=entryPlace["writeCount"]
			# entryPlace["entryCount"]=entryPlace["entryCount"]
			#todo: check if you need to split the file
			if entryPlace["entryCount"]+1>splittingPoint:

				#todo: if file split is needed,
					# 	i. create new fileTracker entries
					# ii. create new file and set it up for new entry

				currentInsertFileData=DataFile(self.tablePath+fileToInsert).getTableData()
				currentInsertFileData.append(data)

				part1 = currentInsertFileData [ :len ( currentInsertFileData ) // 2 ]
				part2=currentInsertFileData[len(currentInsertFileData)//2:]



				x=DataFile(self.tablePath+fileToInsert)
				x.updateTableData(part1)

				fTrackerData.pop(counter-1)
				entryPlace["writeCount"]=len(part1)
				entryPlace["entryCount"]=len(part1)
				fTrackerData.insert(counter-1,entryPlace)



				newFileTrackerEntry = { "keyStart": part2 [ 0 ] [self.primaryKey ],
										"fileName": "data_"+FileUtility.generateRandomString (Var.datafileSuffixLength )+".json",
										"writeCount" : 0,
										"entryCount": len ( part2 )
										}

				newFilePath=self.tablePath+newFileTrackerEntry["fileName"]
				# with open(newFilePath,"w") as json_file:
				# 	dataToWrite=[]
				# 	dataToWrite.append({"key":"null"})
				# 	json.dump(dataToWrite,json_file)

				dataToWrite=[]
				dataToWrite.append ( { "key" : "null" } )
				FileUtility.atomicWriteToFile(filePath = newFilePath,data = dataToWrite)

				x=DataFile(newFilePath)
				x.updateTableData(part2)

				fTrackerData.insert ( counter, newFileTrackerEntry )
			else:


				fTrackerData.pop ( counter - 1 )

				entryPlace["writeCount"]=entryPlace["writeCount"]+1
				entryPlace["entryCount"]=entryPlace["entryCount"]+1

				fTrackerData.insert(counter-1,entryPlace)

				dataFile = DataFile ( self.tablePath + fileToInsert )
				tableData = dataFile.getTableData ( )
				tableData.append ( data )

				dataFile.updateTableData ( tableData )


		#fixme: comment the next block out later
		#todo: update fileTracker if necessary
		fTracker.updateTrackerData (fTrackerData )


		return

	def vanillaSelect( self, fields=None ):

		fileTracker=FileTracker(self.fileTrackerPath)
		fileTrackerData=fileTracker.getTrackerData()
		finalData=[]
		if fields is None:
			fields=list(fileTrackerData[0].keys())
			print("fields: ",fields)
		for trackerData in fileTrackerData:
			dataFilePath=self.tablePath+trackerData["fileName"]
			data=[]
			data=DataFile(dataFilePath).getTableData()
			filteredDict=[dict ((key,x[key]) for key in fields if key in x) for x in data ]
			finalData.extend(filteredDict)




		print(finalData)

		return TempResult(finalData)
		# return finalData


	def equalitySearch( self, fields=None, values=None):

		if fields is None:
			fields=[]
		if values is None:
			values=[]

		fileTracker=FileTracker(self.fileTrackerPath)
		fileTrackerData=fileTracker.getTrackerData()
		finalData=[]
		columns = list ( fileTrackerData [ 0 ].keys ( ) )
		# print ( "columns: ", columns )
		for trackerData in fileTrackerData:
			dataFilePath=self.tablePath+trackerData["fileName"]
			data=[]
			data=DataFile(dataFilePath).getTableData()
			# filteredDict=[ for x in data ]
			for x in data:
				for (field, value) in zip ( fields, values ) :
					# print ( field, value )
					if(x[field] == value):
						print ( x[field], value )
						finalData.append(x)

			# finalData.extend(filteredDict)



		print(finalData)
		return TempResult(finalData)
		# return finalData




if __name__ == '__main__':
	# os.system('rm -rf "/Users/sxs2561/Documents/OneDrive - The Pennsylvania State University/Course Work/cse_541/project/databases/db1/table1"')
	db = Database ( "db1" )
	db.createDbDirectory()
	y=Table(tableName = "table1",dbName = "db1")
	y.createTable()
	print ( "Primary KEY:" + y.getPrimaryKey ( ) )
	y.setPrimaryKey(primaryKey ="nconst" )
	print (  "\nPrimary KEY:" +y.getPrimaryKey ( ) )
	jsonFilePath="/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/inputs/name_basics.json"
	data=FileUtility.readJsonFile(jsonFilePath)
	splittingPoint=3
	for x in data:
		y.insert(x,splittingPoint)

	y.vanillaSelect( fields = [ "nconst", "primaryName" ] )