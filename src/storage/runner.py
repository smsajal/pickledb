from src.storage.table import Table as dbTable
import src.interfaces.storageInterface as interface

if __name__ == '__main__':
	# os.system('rm -rf "/Users/sxs2561/Documents/OneDrive - The Pennsylvania State University/Course Work/cse_541/project/databases/db1/table1"')
	# db = Database ( "db1" )
	# db.createDbDirectory()
	# y=dbTable(tableName = "table1",dbName = "db2")
	# y.createTable()
	# y.setPrimaryKey(primaryKey ="nconst" )
	# jsonFilePath="/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/inputs/name_basics.json"
	# data=FileUtility.readJsonFile(jsonFilePath)
	# splittingPoint=3
	# for x in data:
	# 	y.insert(x,splittingPoint)

	MyTable = dbTable ( tableName = "table1", dbName = "db1" , primaryKey = "nconst")
	# MyTable.vanillaSelect ( ["nconst", "primaryName"] )

	# interface.insert(MyTable, data ={ "nconst"            : "nm0000002", "primaryName" : "Rubaba Hasan", "birthYear" : "1993", "deathYear" : "1987", "primaryProfession" : "soundtrack,actor,miscellaneous","knownForTitles"    : "tt0031983,tt0050419,tt0072308,tt0053137" })

	MyTable.equalitySearch(fields=["birthYear", "deathYear"], values = ["1949", "1982"])