import datetime
import src.cache.cache as cache
import src.interfaces.queryEngine as QueryEngine
def executeQuery(query):
	a=datetime.datetime.now()
	print("=========== query: ",query)
	cache.cache_checkQuery(query)
	# result=eval(query)

	b=datetime.datetime.now()
	duration=b-a
	print ( "=========== query: ", query )
	# print(type(duration.microseconds))
	return duration.microseconds