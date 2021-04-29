import datetime
import src.interfaces.queryEngine as QueryEngine
from src.storage.table import Table
from src.storage.tempResult import TempResult
from src.storage.join import sortedMergeJoin, hashJoin, nestedLoopJoin

movies = TempResult(Table(tableName="imdb_movies", dbName="imdb_kaggle_small").vanillaSelect())
names = TempResult(Table(tableName="imdb_names", dbName="imdb_kaggle_small").vanillaSelect())
ratings = TempResult(Table(tableName="imdb_ratings", dbName="imdb_kaggle_small").vanillaSelect())
title_principals = TempResult(Table(tableName="title_principals", dbName="imdb_kaggle_small").vanillaSelect())

def executeQuery(query):
	a=datetime.datetime.now()

	result=eval(query)
	# print("~~~~~~~~~~~ result type: ",type(result))
	# print(result)
	b=datetime.datetime.now()
	duration=b-a
	print ( "=========== query: ", query )
	# print(type(duration.microseconds))
	durationNanoSeconds=duration.total_seconds()*1000000000
	return durationNanoSeconds