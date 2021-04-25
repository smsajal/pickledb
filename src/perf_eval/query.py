import datetime
import src.interfaces.queryEngine as QueryEngine
def executeQuery(query):
	a=datetime.datetime.now()
	print("=========== query: ",query)
	result=eval(query)
	b=datetime.datetime.now()
	duration=b-a
	print(type(duration.microseconds))
	return duration.microseconds