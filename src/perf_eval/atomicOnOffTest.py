import random

import numpy as np

import datetime
import src.storage.fileUtility as FileUtility
from src.perf_eval.query import executeQuery
import src.interfaces.queryEngine as QueryEngine
from src.storage.table import Table
from src.storage.tempResult import TempResult

def atomicOnTest():

	configFile="/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/src/perf_eval/config.json"
	workloadFile="/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/src/perf_eval/tempWorkload.json"
	latencyRecordFile="/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/src/perf_eval/latencies.json"

	configuration=FileUtility.readJsonFile(configFile)
	queries=FileUtility.readJsonFile(workloadFile)

	# fixme: separate read and write queries in different files
	readQueries=queries["readQueries"]
	writeQueries=queries["writeQueries"]

	latencies={}
	expCount=0

	for config in configuration:

		totalQueriesCount=config["totalQueries"]
		readPercentage=config["readPercentage"]
		writePercentage=1-readPercentage

		queryChoices=[np.random.choice(np.arange(0,2),p=[readPercentage,writePercentage]) for i in range(totalQueriesCount)]


		readQueriesCount=queryChoices.count(0)
		writeQueriesCount=queryChoices.count(1)

		readQueriesToRun=random.choices(readQueries,k=readQueriesCount)

		writeQueryIndexes=random.sample(range(0,writeQueriesCount),writeQueriesCount)
		writeQueriesToRun=[writeQueries[x] for x in writeQueryIndexes]

		print(" ********  read-queries count: ",len(readQueriesToRun)," write-queries count: ",len(writeQueriesToRun))


		latency=[]
		readIndex=0
		writeIndex=0
		for i in queryChoices:
			if i==0:
				query=readQueriesToRun[readIndex]
				readIndex+=1
			else:
				query=writeQueriesToRun[writeIndex]
				writeIndex+=1
			latency.append(executeQuery(query))

		expCount+=1
		latencies[str(expCount)]=latency

	FileUtility.writeToJsonFile(latencyRecordFile,data=latencies)


if __name__ == '__main__':
    atomicOnTest()