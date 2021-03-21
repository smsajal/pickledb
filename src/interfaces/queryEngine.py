import src.interfaces.storageInterface as storageInterface
from src.storage.table import Table as dbTable
import json

def createDatabase(dbName):
    db = storageInterface.createDatabase(dbName)
    if (db):
        print("DataBase Created Successfully!")

def createTable(dbName,tableName):
    table = storageInterface.createTable(dbName,tableName)
    if (table):
        print("Table Created Successfully!")

def bulkInsertTable(tableObj,bulkData):
    bulkDataList = json.loads(bulkData)
    storageInterface.bulkInsert(tableObj,bulkDataList)
    print("Bulk Insert Completed Successfully!")

def bulkInsertTableJSON(tableObj,bulkDataJSONpath):
    file = open(bulkDataJSONpath)
    bulkDataList = json.load(file)
    storageInterface.bulkInsert(tableObj, bulkDataList)
    print("Bulk Insert Completed Successfully!")

def tableInsert(tableObj,data):
    dataList = json.loads(data)
    storageInterface.insert(tableObj,dataList)
    print("Single Tuple Insert Completed Successfully!")

def simpleSelect(tableObj,fields):
    fields_list = list(fields.split(","))
    print("Select Values are as follows: ")
    tableObj.vanillaSelect(fields_list)

def interface():
    print(30 * '-')
    print("   M A I N - M E N U")
    print(30 * '-')
    print("1. Create DataBase")
    print("2. Create Table")
    print("3. Bulk Insert Into Table")
    print("4. Bulk Insert Into Table from JSON file")
    print("5. Single Insert Into Table")
    print("6. Select Columns from Table")
    print("7. Quit")
    print(30 * '-')
    choice = int(input("Enter your choice [1-7]: "))
    return choice

def interfaceCalls(choice):
    if (choice == 1):                     #DB creation
        dbName = input("Enter the name of the DataBase: ")
        createDatabase(dbName)
    elif (choice == 2):                   # Table creation in DB
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table: ")
        createTable(dbName, tableName)
    elif (choice == 3):                   # Bulk Insert in Table
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        primaryKey = input("Enter the Primary Key Field: ")
        TableObj = dbTable( tableName = tableName, dbName = dbName , primaryKey = primaryKey)
        bulkData = input("Enter the Bulk Data is the form of a JSON array: ")
        bulkInsertTable(TableObj,bulkData)
    elif (choice == 4):                 # Bulk Insert in Table from JSON file
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        primaryKey = input("Enter the Primary Key Field: ")
        TableObj = dbTable(tableName=tableName, dbName=dbName, primaryKey=primaryKey)
        bulkDataPath = input("Enter the path to the JSON file: ")
        bulkInsertTableJSON(TableObj,bulkDataPath)
    elif (choice == 5):                    # Single Tuple Insert in table
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        primaryKey = input("Enter the Primary Key Field: ")
        TableObj = dbTable(tableName=tableName, dbName=dbName, primaryKey=primaryKey)
        singleData = input("Enter the Single Data Row is the form of a JSON object: ")
        tableInsert(TableObj,singleData)
    elif (choice == 6):                    # Simple Select from Table
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        primaryKey = input("Enter the Primary Key Field: ")
        TableObj = dbTable(tableName=tableName, dbName=dbName, primaryKey=primaryKey)
        columns = input("Enter the columns separated by a ',': ")
        simpleSelect(TableObj,columns)
    elif (choice == 7):                   #Quit
        print("QUIT")
    else:                                 #Invalid Choice
        print("Invalid Choice.")

def main():
        choice = 0
        while (choice < 7):
            choice = interface()
            interfaceCalls(choice)

if __name__ == "__main__":
    main()