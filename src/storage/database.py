# import variables as Var
import src.storage.variables as Var
import os
class Database:
	def __init__(self,name):
		self.dbName=name
		# self.createDbDirectory()

	def createDbDirectory( self ):
		dbPath=os.path.join(Var.databaseStorageFilePath,self.dbName)
		print("creating directory: ",dbPath)
		os.mkdir(path = dbPath)

	def getDatabaseName( self ):
		return self.dbName


if __name__ == '__main__':
	x=Database("db1")
	x.createDbDirectory()
