import storageInterface as storageInterface
from src.storage.table import Table as dbTable

def createDatabase(dbName):
    storageInterface.createDatabase(dbName)

def createTable(dbName,tableName):
    storageInterface.createTable(dbName,tableName)

def bulkInsertTable(tableObj,bulkData):
    storageInterface.bulkInsert(tableObj,bulkData)

def tableInsert(tableObj,data):
    storageInterface.insert(tableObj,data)

def simpleSelect(tableObj,fields):
    tableObj.vanillaSelect(fields)

def main():
    #createDatabase("db2")
    #createTable("db2","table1")
    MyTable = dbTable ( tableName = "table1", dbName = "db2" , primaryKey = "nconst")
    #tableInsert(MyTable,{"nconst": "nm0000001", "primaryName": "Fred Astaire", "birthYear": "1899", "deathYear": "1987", "primaryProfession": "soundtrack,actor,miscellaneous", "knownForTitles": "tt0031983,tt0050419,tt0072308,tt0053137"})
    #bulkInsertTable(MyTable,[{"nconst": "nm0000005", "primaryName": "Ingmar Bergman", "birthYear": "1918", "deathYear": "2007", "primaryProfession": "writer,director,actor", "knownForTitles": "tt0050976,tt0060827,tt0069467,tt0050986"}, {"nconst": "nm0000006", "primaryName": "Ingrid Bergman", "birthYear": "1915", "deathYear": "1982", "primaryProfession": "actress,soundtrack,producer", "knownForTitles": "tt0038109,tt0034583,tt0038787,tt0077711"}])

    simpleSelect(MyTable,fields = ["nconst", "primaryName"])

if __name__ == "__main__":
    main()