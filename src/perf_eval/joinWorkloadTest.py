import random

import numpy as np

import datetime
import src.storage.fileUtility as FileUtility
from src.perf_eval.query import executeQuery
import src.interfaces.queryEngine as QueryEngine

def joinTest():

	configFile = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/src/perf_eval/joinConfig.json"
	workloadFile = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/src/perf_eval/joinWorkload.json"
	latencyRecordFile = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/src/perf_eval/joinLatency.json"


	configuration=FileUtility.readJsonFile(configFile)
	queries=FileUtility.readJsonFile(workloadFile)

	# fixme: separate read and write queries in different files
	# mergeJoinQueries=queries[configuration["queryType"]]
	# hashJoinQueries=queries["joinHashQueries"]
	# loopJoinQueries = queries["joinLoopQueries"]

	latencies={}
	expCount=0

	for config in configuration:

		totalQueriesCount=config["totalQueries"]
		joinQueries=queries[config["queryType"]]

		joinQueriesToRun=random.choices(joinQueries,k=totalQueriesCount)

		print(" ********  join-queries count: ",len(joinQueriesToRun))


		latency=[]
		for query in joinQueriesToRun:
			latency.append(executeQuery(query))

		expCount+=1
		latencies[str(expCount)]=latency

	FileUtility.writeToJsonFile(latencyRecordFile,data=latencies)


if __name__ == '__main__':
	a=datetime.datetime.now()
	joinTest()
	b=datetime.datetime.now()
	print("total experiment duration: ",(b-a))
