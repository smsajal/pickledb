import src.interfaces.storageInterface as storageInterface
from src.storage.table import Table as dbTable
from src.storage.tempResult import TempResult as result, TempResult
import src.storage.join as join
import json

def createDatabase(dbName):
    '''
        args:
            dbName: the name of the database to the created

        equivalent to:
            CREATE DATABASE dbName;
    '''
    db = storageInterface.createDatabase(dbName)
    if (db):
        print("DataBase Created Successfully!")

def createTable(dbName,tableName):
    '''
        args:
            dbName: the name of the database to the created
            tableName: the name of the table to be created

        equivalent to:
            CREATE TABLE tableName
    '''
    table = storageInterface.createTable(dbName,tableName)
    if (table):
        print("Table Created Successfully!")

def bulkInsertTable(tableName, dbName, primaryKey, bulkData):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            primaryKey: Primary key of the table
            bulkData: String in the form of a JSON Array

        equivalent to:
            INSERT INTO table_name (column1, column2, column3, ...)
            VALUES (value1, value2, value3, ...),
            (value1, value2, value3, ...), ..., (.....) ;
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName, primaryKey=primaryKey)
    storageInterface.bulkInsert(tableObj,bulkData)
    print("Bulk Insert Completed Successfully!")

def bulkInsertTableJSON(tableName, dbName, primaryKey, bulkDataJSONpath):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            primaryKey: Primary key of the table
            bulkData: .json file containing a JSON Array

        equivalent to:
            INSERT INTO table_name (column1, column2, column3, ...)
            VALUES (value1, value2, value3, ...),
            (value1, value2, value3, ...), ..., (.....) ;
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName, primaryKey=primaryKey)
    file = open(bulkDataJSONpath)
    bulkDataList = json.load(file)
    storageInterface.bulkInsert(tableObj, bulkDataList)
    print("Bulk Insert Completed Successfully!")

def tableInsert(tableName,dbName,primaryKey,data):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            primaryKey: Primary key of the table
            bulkData: String in the form of a JSON Object

        equivalent to:
            INSERT INTO table_name (column1, column2, column3, ...)
            VALUES (value1, value2, value3, ...);
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName, primaryKey=primaryKey)
    storageInterface.insert(tableObj,data)
    print("Single Tuple Insert Completed Successfully!")


def simpleSelect(tableName,dbName,primaryKey,fields=None):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            primaryKey: Primary key of the table
            fields: List of attributes

        equivalent to:
            SELECT column1, column2, ...
            FROM table_name;
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName, primaryKey=primaryKey)

    if not (fields is None):
        fields_list = list(fields.split(","))
        print("Select Values are as follows: ")
        x = TempResult(tableObj.vanillaSelect(fields_list))
        x.print()
        toReturn = x.data
    else:
        x = TempResult(tableObj.vanillaSelect())
        x.print()
        toReturn = x.data
    return toReturn


def sample(tableName,dbName,sampleSize):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            sampleSize: number of rows to be sampled
    '''
    if sampleSize > 0:
        tableObj = dbTable(tableName=tableName, dbName=dbName)
        sampleResult = result(tableObj.vanillaSelect()).sample(sampleSize)
        print(sampleResult.data)
        print("Sample Result Length: ", len(sampleResult.data))
        return sampleResult.data

def limitResult(tableName,dbName,limit):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            limit: number of rows to be sampled as limit
    '''
    if limit > 0:
        tableObj = dbTable(tableName=tableName, dbName=dbName)
        limitResult = result(tableObj.vanillaSelect()).limit(limit)
        print(limitResult.data)
        print("Limit Result length: ", len(limitResult.data))
        return limitResult.data

def orderBy(tableName,dbName,field,limit=0):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            field: attribute name to be used in OrderBy
            limit: number of rows to be sampled as limit
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName)

    if (limit == 0):
        selectResult = result(tableObj.vanillaSelect())

    else:
        selectResult = result(tableObj.vanillaSelect()).limit(limit)

    orderResult = selectResult.orderBy(field=field)
    print(orderResult.data)
    print("Order Result Length: ", len(orderResult.data))
    return orderResult.data

# mean(limitCount=100)
# limit(limitCount=100).mean()
def mean(tableName,dbName,field,limit=0):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            field: attribute name to be used in finding Mean
            limit: number of rows to be sampled as limit
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName)

    if (limit == 0):
        selectResult = result(tableObj.vanillaSelect())

    else:
        selectResult = result(tableObj.vanillaSelect()).limit(limit)

    meanResult = selectResult.mean(field=field)
    print("Mean: ", meanResult)
    return meanResult

def median(tableName,dbName,field,limit=0):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            field: attribute name to be used in finding Median
            limit: number of rows to be sampled as limit
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName)

    if (limit == 0):
        selectResult = result(tableObj.vanillaSelect())

    else:
        selectResult = result(tableObj.vanillaSelect()).limit(limit)

    medianResult = selectResult.median(field=field)
    print("Median: ", medianResult)
    return medianResult

def min(tableName,dbName,field,limit=0):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            field: attribute name to be used in finding Min
            limit: number of rows to be sampled as limit
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName)

    if (limit == 0):
        selectResult = result(tableObj.vanillaSelect())

    else:
        selectResult = result(tableObj.vanillaSelect()).limit(limit)
    min = selectResult.min(field=field)
    print("Min: ", min)
    return min

def max(tableName,dbName,field,limit=0):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            field: attribute name to be used in finding Max
            limit: number of rows to be sampled as limit
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName)

    if (limit == 0):
        selectResult = result(tableObj.vanillaSelect())

    else:
        selectResult = result(tableObj.vanillaSelect()).limit(limit)

    max = selectResult.max(field=field)
    print("Max: ", max)
    return max

def stdDev(tableName,dbName,field,limit=0):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            field: attribute name to be used in finding Standard Deviation
            limit: number of rows to be sampled as limit
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName)

    if (limit == 0):
        selectResult = result(tableObj.vanillaSelect())

    else:
        selectResult = result(tableObj.vanillaSelect()).limit(limit)
    stddev = selectResult.stdDev(field=field)
    print("Standard Dev: ", stddev)
    return stddev

def sum(tableName,dbName,field,limit=0):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            field: attribute name to be used in finding Sum
            limit: number of rows to be sampled as limit
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName)

    if (limit == 0):
        selectResult = result(tableObj.vanillaSelect())

    else:
        selectResult = result(tableObj.vanillaSelect()).limit(limit)
    sum = selectResult.sum(field=field)
    print("Sum: ", sum)
    return sum

def count(tableName,dbName,limit):
    '''
        args:
            tableName: Name of the table
            dbName: Name of the database
            field: attribute name to be used in finding Count
            limit: number of rows to be sampled as limit
    '''
    tableObj = dbTable(tableName=tableName, dbName=dbName)

    if limit == 0:
        selectResult = result(tableObj.vanillaSelect())
    else:
        selectResult = result(tableObj.vanillaSelect()).limit(limit)
    count = selectResult.count()
    print("count: ",count)

def nestedLoopJoin(dbName,table1,table2,commonField,commonLimit=0):
    '''
        args:
            dbName: Name of the database
            table1: Name of first table
            table2: Name of second table
            commonField: Name of the common attribute between table1 and table2
            commonLimit: number of rows to be sampled from table1 and table2 as limit
    '''
    tableObj1 = dbTable(tableName=table1, dbName=dbName)
    tableObj2 = dbTable(tableName=table2, dbName=dbName)
    if commonLimit == 0:
        TableSet1 = result(tableObj1.vanillaSelect())
        TableSet2 = result(tableObj2.vanillaSelect())
    else:
        TableSet1 = result(tableObj1.vanillaSelect()).limit(commonLimit)
        TableSet2 = result(tableObj2.vanillaSelect()).limit(commonLimit)
    nestedLoopResult = join.nestedLoopJoin(tempResult1=TableSet1, joinField1=commonField, tempResult2=TableSet2, joinField2=commonField)
    nestedLoopResult.print()
    print("Size of Nested Loop Join Result: ", len(nestedLoopResult.data))
    return nestedLoopResult.data

def hashJoin(dbName,table1,table2,commonField,commonLimit=0):
    '''
        args:
            dbName: Name of the database
            table1: Name of first table
            table2: Name of second table
            commonField: Name of the common attribute between table1 and table2
            commonLimit: number of rows to be sampled from table1 and table2 as limit
    '''
    tableObj1 = dbTable(tableName=table1, dbName=dbName)
    tableObj2 = dbTable(tableName=table2, dbName=dbName)
    if commonLimit == 0:
        TableSet1 = result(tableObj1.vanillaSelect())
        TableSet2 = result(tableObj2.vanillaSelect())
    else:
        TableSet1 = result(tableObj1.vanillaSelect()).limit(commonLimit)
        TableSet2 = result(tableObj2.vanillaSelect()).limit(commonLimit)
    hashJoinResult = join.hashJoin(tempResult1=TableSet1, joinField1=commonField, tempResult2=TableSet2, joinField2=commonField)
    # hashJoinResult.print()
    print(hashJoinResult.data)
    print("Size of Hash Join Result: ", len(hashJoinResult.data))
    return hashJoinResult.data

def sortedMergeJoin(dbName,table1,table2,commonField,commonLimit=0):
    '''
        args:
            dbName: Name of the database
            table1: Name of first table
            table2: Name of second table
            commonField: Name of the common attribute between table1 and table2
            commonLimit: number of rows to be sampled from table1 and table2 as limit
    '''
    tableObj1 = dbTable(tableName=table1, dbName=dbName)
    tableObj2 = dbTable(tableName=table2, dbName=dbName)
    if commonLimit == 0:
        TableSet1 = result(tableObj1.vanillaSelect())
        TableSet2 = result(tableObj2.vanillaSelect())
    else:
        TableSet1 = result(tableObj1.vanillaSelect()).limit(commonLimit)
        TableSet2 = result(tableObj2.vanillaSelect()).limit(commonLimit)
    sortMergeResult = join.sortedMergeJoin(tempResult1=TableSet1, joinField1=commonField, tempResult2=TableSet2, joinField2=commonField)
    sortMergeResult.print()
    print("Size of Sort Merge Join Result: ", len(sortMergeResult.data))
    return sortMergeResult.data



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
    print("7. Sample")
    print("8. Limit")
    print("9. OrderBy")
    print("10. Mean")
    print("11. Median")
    print("12. Min")
    print("13. Max")
    print("14. Standard Deviation")
    print("15. Sum")
    print("16. Count")
    print("17. Nested Loop Join")
    print("18. Hash Join")
    print("19. Sorted Merge Join")
    print("20. Quit")
    print(30 * '-')
    choice = int(input("Enter your choice [1-20]: "))
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
        bulkData = input("Enter the Bulk Data is the form of a JSON array: ")
        bulkData = json.loads(bulkData)
        bulkInsertTable(tableName, dbName, primaryKey, bulkData)
    elif (choice == 4):                 # Bulk Insert in Table from JSON file
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        primaryKey = input("Enter the Primary Key Field: ")
        bulkDataPath = input("Enter the path to the JSON file: ")
        bulkInsertTableJSON(tableName, dbName, primaryKey, bulkDataPath)
    elif (choice == 5):                    # Single Tuple Insert in table
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        primaryKey = input("Enter the Primary Key Field: ")
        singleData = input("Enter the Single Data Row is the form of a JSON object: ")
        singleData = json.loads(singleData)
        tableInsert(tableName,dbName,primaryKey,singleData)
    elif (choice == 6):                    # Simple Select from Table
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        primaryKey = input("Enter the Primary Key Field: ")
        columns = input("Enter the columns separated by a ',': ")
        simpleSelect(tableName,dbName,primaryKey,columns)
    elif (choice == 7):                     # Sample
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        sampleSize = input("Enter the data Sample size (>0): ")
        sample(tableName, dbName, sampleSize)
    elif (choice == 8):                     # Limit
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        limitSize = int(input("Enter the data Limit (>0): "))
        limitResult(tableName,dbName,limitSize)
    elif (choice == 9):                     # orderBy
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        field = input("Enter the field name: ")
        limit = int(input("Enter the data Limit (0 = No Limit): "))
        orderBy(tableName, dbName, field, limit)
    elif (choice == 10):                    # mean
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        field = input("Enter the field name: ")
        limit = int(input("Enter the data Limit (0 = No Limit): "))
        mean(tableName, dbName, field, limit)
    elif (choice == 11):                    # median
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        field = input("Enter the field name: ")
        limit = int(input("Enter the data Limit (0 = No Limit): "))
        median(tableName, dbName, field, limit)
    elif (choice == 12):                    # min
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        field = input("Enter the field name: ")
        limit = int(input("Enter the data Limit (0 = No Limit): "))
        min(tableName, dbName, field, limit)
    elif (choice == 13):                    # max
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        field = input("Enter the field name: ")
        limit = int(input("Enter the data Limit (0 = No Limit): "))
        max(tableName, dbName, field, limit)
    elif (choice == 14):                    # std dev
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        field = input("Enter the field name: ")
        limit = int(input("Enter the data Limit (0 = No Limit): "))
        stdDev(tableName, dbName, field, limit)
    elif (choice == 15):                    # sum
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        field = input("Enter the field name: ")
        limit = int(input("Enter the data Limit (0 = No Limit): "))
        sum(tableName, dbName, field, limit)
    elif (choice == 16):                    # count
        dbName = input("Enter the name of the DataBase to be used: ")
        tableName = input("Enter the name of the Table to be used: ")
        limit = int(input("Enter the data Limit (0 = No Limit): "))
        count(tableName, dbName, limit)
    elif (choice == 17):                    # nested loop join
        dbName = input("Enter the name of the DataBase to be used: ")
        table1 = input("Enter the name of the First Table to be used: ")
        table2 = input("Enter the name of the Second Table to be used: ")
        commonField = input("Enter the Common Field name : ")
        commonLimit = int(input("Enter the data Limit (0 = No Limit): "))
        nestedLoopJoin(dbName, table1, table2, commonField, commonLimit)
    elif (choice == 18):                    # hash join
        dbName = input("Enter the name of the DataBase to be used: ")
        table1 = input("Enter the name of the First Table to be used: ")
        table2 = input("Enter the name of the Second Table to be used: ")
        commonField = input("Enter the Common Field name : ")
        commonLimit = int(input("Enter the data Limit (0 = No Limit): "))
        hashJoin(dbName, table1, table2, commonField, commonLimit)
    elif (choice == 19):                    # sorted merge join
        dbName = input("Enter the name of the DataBase to be used: ")
        table1 = input("Enter the name of the First Table to be used: ")
        table2 = input("Enter the name of the Second Table to be used: ")
        commonField = input("Enter the Common Field name : ")
        commonLimit = int(input("Enter the data Limit (0 = No Limit): "))
        sortedMergeJoin(dbName, table1, table2, commonField, commonLimit)
    elif (choice == 20):                    # Quit
        print("QUIT")
    else:                                   # Invalid Choice
        print("Invalid Choice.")

def main():
    choice = 0
    while (choice < 20):
        choice = interface()
        interfaceCalls(choice)

    # simpleSelect(tableName = "tablex", dbName = "dbx", primaryKey = "nconst")

    # limitResult(tableName = "imdb_movies", dbName = "imdb_kaggle_small", limit = 5)
    #
    # orderBy(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "country")
    # orderBy(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "title", limit = 5)
    #
    # sample(tableName = "imdb_movies", dbName = "imdb_kaggle_small", sampleSize = 5)
    #
    # mean(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration")
    # mean(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 5)
    #
    # median(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 0)
    # median(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 5)
    #
    # min(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 0)
    # min(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 5)
    #
    # max(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 0)
    # max(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 5)
    #
    # stdDev(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 0)
    # stdDev(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 5)
    #
    # sum(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 0)
    # sum(tableName = "imdb_movies", dbName = "imdb_kaggle_small", field = "duration", limit = 5)
    #
    # count(tableName = "imdb_movies", dbName = "imdb_kaggle_small", limit= 0)
    # count(tableName="imdb_movies", dbName="imdb_kaggle_small", limit=5)
    #
    # nestedLoopJoin(dbName="imdb_kaggle_small", table1="imdb_movies", table2="imdb_ratings", commonField="imdb_title_id", commonLimit= 0)
    # nestedLoopJoin(dbName="imdb_kaggle_small", table1="imdb_movies", table2="imdb_ratings", commonField="imdb_title_id", commonLimit=5)
    #
    # hashJoin(dbName="imdb_kaggle_small", table1="imdb_movies", table2="imdb_ratings", commonField="imdb_title_id", commonLimit= 0)
    # hashJoin(dbName="imdb_kaggle_small", table1="imdb_movies", table2="imdb_ratings", commonField="imdb_title_id", commonLimit=5)
    #
    # sortedMergeJoin(dbName="imdb_kaggle_small", table1="imdb_movies", table2="imdb_ratings", commonField="imdb_title_id", commonLimit= 0)
    # sortedMergeJoin(dbName="imdb_kaggle_small", table1="imdb_movies", table2="imdb_ratings", commonField="imdb_title_id", commonLimit=5)
    #

if __name__ == "__main__":
    main()