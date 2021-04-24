import random

import numpy as np

import datetime
import src.storage.fileUtility as FileUtility
from src.storage.table import Table
from src.storage.tempResult import TempResult



movies = TempResult ( Table ( tableName = "imdb_movies", dbName = "imdb_kaggle_small" ).vanillaSelect ( ) )
names = TempResult ( Table ( tableName = "imdb_names", dbName = "imdb_kaggle_small" ).vanillaSelect ( ) )
ratings = TempResult ( Table ( tableName = "imdb_ratings", dbName = "imdb_kaggle_small" ).vanillaSelect ( ) )
title_principals = TempResult (Table ( tableName = "title_principals", dbName = "imdb_kaggle_small" ).vanillaSelect ( ) )

def executeQuery(query):
	a=datetime.datetime.now()
	eval(query)
	b=datetime.datetime.now()
	duration=b-a
	print(type(duration.microseconds))
	return duration.microseconds

def test1():
	data = FileUtility.readJsonFile (
		"/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/src/perf_eval/readWorkload.json" )
	readContent = data [ "readQueries" ]
	print ( readContent )

	movies = TempResult ( Table ( tableName = "imdb_movies", dbName = "imdb_kaggle_small" ).vanillaSelect ( ) )
	names = TempResult ( Table ( tableName = "imdb_names", dbName = "imdb_kaggle_small" ).vanillaSelect ( ) )
	ratings = TempResult ( Table ( tableName = "imdb_ratings", dbName = "imdb_kaggle_small" ).vanillaSelect ( ) )
	title_principals = TempResult (
		Table ( tableName = "title_principals", dbName = "imdb_kaggle_small" ).vanillaSelect ( ) )
	# table1=TempResult(table.vanillaSelect())
	for x in readContent :
		executeQuery ( x )

def test2():
	configurations=FileUtility.readJsonFile("/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/src/perf_eval/config.json")
	queries=FileUtility.readJsonFile("/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/src/perf_eval/readWorkload.json" )
	readQueries=queries["readQueries"]
	writeQueries=queries["writeQueries"]

	latencies={}
	expCount=0
	for config in configurations:

		totalQueriesCount=config["totalQueries"]
		readPercentage=config["readPercentage"]
		writePercentage=1-readPercentage
		# readQueriesCount=int(totalQueriesCount*readPercentage)
		# writeQueriesCount=int(totalQueriesCount-readQueriesCount)



		queryChoices=[]
		for i in range(totalQueriesCount):
			queryChoices.append(np.random.choice(np.arange(0,2),p=[readPercentage,writePercentage]))




		readQueriesCount=queryChoices.count(0)
		writeQueriesCount=queryChoices.count(1)
		print ( len ( readQueries ), " ~~~~~ ", readQueriesCount )
		readQueriesToRun=random.choices(readQueries,k=readQueriesCount)
		writeQuerySequence=random.sample(range(0,writeQueriesCount),writeQueriesCount)

		print("readcount: ",readQueriesCount, "writeCount: ",writeQueriesCount)

		latency = [ ]
		readIndex=0
		writeIndex=0
		for i in queryChoices:

			if i==0:
				query=readQueriesToRun[readIndex]
				readIndex+=1

			else:
				query=writeQueries[writeQuerySequence[writeIndex]]
				writeIndex+=1
			latency.append(executeQuery(query))


		expCount+=1
		latencies[str(expCount)]=latency
		print(latency)

	FileUtility.writeToJsonFile("/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/src/perf_eval/latencies.json",data = latencies)
	return

if __name__ == '__main__':
	test2()