import datetime
import src.storage.fileUtility as FileUtility
from src.storage.table import Table
from src.storage.tempResult import TempResult


def executeQuery(query):
	a=datetime.datetime.now()
	eval(query)
	b=datetime.datetime.now()
	duration=b-a
	print(duration.microseconds)
	return duration.microseconds

if __name__ == '__main__':
	data=FileUtility.readJsonFile("/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/src/perf_eval/readWorkload.json")
	readContent=data["readQueries"]
	print(readContent)

	table = Table ( tableName = "imdb_movies", dbName = "imdb_kaggle_small" )
	table1=TempResult(table.vanillaSelect())
	executeQuery(readContent[0])
	executeQuery(readContent[1])