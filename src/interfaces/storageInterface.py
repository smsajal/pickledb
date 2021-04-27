import src.storage.variables as StorageVariables
from src.storage.database import Database as Database
from src.storage.table import Table as Table

def createDatabase(databaseName):
	'''
		args:
			databaseName: the name of the database to the created

		returns:
			db: Database object created
	'''
	db=Database(databaseName)
	db.createDbDirectory()
	return db


def createTable(databaseName, tableName):
	'''
		args:
			databaseName: name of the database
			tableName: name of the table

		returns:
			table: Table object created

	'''
	table=Table(tableName,databaseName)
	table.createTable()
	return table

def bulkInsert(table,data):
	'''
		args:
			table: Table object for the table where data to be inserted
			data: data in the form of json array to be inserted in the table

		returns:
			None
	'''
	for x in data:
		table.insert( x, StorageVariables.bulkInsertOccupancyCount )

	return

def insert(table,data):
	'''
		args:
			table: Table object for the table where data to be inserted
			data: data in the form of json object to be inserted into the table
		returns:
			None
	'''

	# print("---------- data type: ",type(data))
	# print("------------ occupancyCount type: ",type(StorageVariables.singleInsertOccupancyCount))
	table.insert(data,StorageVariables.singleInsertOccupancyCount)
	return



