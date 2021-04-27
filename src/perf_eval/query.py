import datetime
import src.interfaces.queryEngine as QueryEngine
def executeQuery(query):
	a=datetime.datetime.now()

	result=eval(query)
	# print("~~~~~~~~~~~ result type: ",type(result))
	# print(result)
	b=datetime.datetime.now()
	duration=b-a
	print ( "=========== query: ", query )
	# print(type(duration.microseconds))
	return duration.microseconds