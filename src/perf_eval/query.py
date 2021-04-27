import datetime
import src.cache.caheDict as cache
import src.interfaces.queryEngine as QueryEngine
def executeQuery(query):
	a=datetime.datetime.now()
	print("=========== query: ",query)
	cache.cache_checkQuery(query)
	# result=eval(query)
	# print("~~~~~~~~~~~ result type: ",type(result))
	# print(result)
	b=datetime.datetime.now()
	duration=b-a
	# print(type(duration.microseconds))
	durationNanoSeconds = duration.total_seconds() * 1000000000
	return durationNanoSeconds