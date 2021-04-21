from random import sample
import statistics
import datetime
from src.storage.table import Table as Table


'''
	variables:
		data = the data of the tempResult
		fieldNames = names of fields of the data
'''
class TempResult():

	'''
		args:
			data = a list of json objects, json keys would be table field name
	'''
	def __init__(self,data):
		self.data=data
		self.fieldNames=list(data[0].keys())

	def getData( self ):
		return self.data

	def vanillaSelect( self, fields=None, limit=None ):
		'''
			args:
				fields: list of strings, denotes of the names of fields to select
				limit: int, specifies number of rows to return
		'''
		selectData=[]

		if fields is None:
			fields=self.fieldNames
		if limit is None:
			limit=len(self.data)

		for dataPoint in self.data:
			selectData=[dict((key,x[key]) for key in fields if key in x) for x in self.data]

		return TempResult(selectData[:limit])

	def equalitySearch( self, fields=None, values=None ):
		'''
			args:
				fields: list of strings, denotes of the names of fields to select
				limit: int, specifies number of rows to return
		'''
		if fields is None:
			fields=[]
		if values is None:
			values=[]

		columns=self.fieldNames
		finalData=[]
		for x in self.data:
			for (field,value) in zip(fields,values):
				if(x[field]==value):
					finalData.append(x)

		return TempResult(finalData)

	def limit( self,limitCount=None ):
		if limitCount is None:
			limitCount=len(self.data)
		return TempResult(self.data[:limitCount])


	def orderBy( self, field=None ):
		if field is None:
			print("no fields selected, invalid operation")
			return
		if not (field in self.fieldNames) :
			print("invalid field name")
			return

		orderedData=sorted(self.data,key = lambda i:i[field])

		return TempResult(orderedData)

	def sample( self, sampleCount=None ):
		if sampleCount is None:
			return TempResult(self.data)

		sampledData=sample(self.data,sampleCount)

		return TempResult(sampledData)



	def mean( self, field=None ):
		if field is None:
			print("invalid field name")
			return

		meanValue=float(self.sum(field = field)/len(self.data))

		return meanValue

	def median( self,field=None ):
		if field is None:
			print("invalid field name")
			return
		dataPoints=[float(x[field]) for x in self.data]
		return statistics.median(dataPoints)

	def min( self,field=None ):
		if field is None:
			print("invalid field name")
			return

		return min([float(x[field]) for x in self.data])


	def max( self,field=None ):
		if field is None:
			print("invalid field name")
			return

		return max([float(x[field]) for x in self.data])

	def stdDev( self,field=None ):
		if field is None:
			print("invalid field name")
			return

		return statistics.stdev([float(x[field]) for x in self.data])

	def count( self ):
		return len(self.data)

	def sum( self,field=None ):
		if field is None:
			print("invalid field name")
			return

		return sum( float(x[field ]) for x in  self.data)
	def print( self ):
		print("------------------------------------")
		for x in self.data:
			print(x)
		print ( "------------------------------------" )
		return
#todo: test these functions

def main():
	a = datetime.datetime.now ( )
	# todo: create a table
	table=Table(tableName="imdb_movies", dbName="imdb_kaggle_big")
	# todo: get vanilla select on table => result1
	# table.vanillaSelect()
	select1Result=TempResult(table.vanillaSelect())
	# todo: do equality search on table => result2
	# todo: do limit on result1 and result2
	limit1Result=select1Result.limit(limitCount = 50000)
	print(len(limit1Result.data))
	# todo: do orderBy on result1 and result2
	order1Result=limit1Result.orderBy(field = "title")
	# order1Result.print()
	# todo: sample on result1 and result2
	sample1Result=order1Result.sample(sampleCount = 50000)

	# todo: mean on result1 and result2
	mean1=sample1Result.mean(field = "duration")
	print("mean duration: ",mean1)
	# todo: median on result1 and result2
	median1=sample1Result.median(field = "duration")
	print("median duration: ",median1)
	# todo: min on result1 and result2
	min1=sample1Result.min(field = "duration")
	print("min duration: ",min1)
	# todo: max on result1 and result2
	max1=sample1Result.max(field = "duration")
	print("max duration: ",max1)
	# todo: stdDev on result1 and result2
	stdDev1=sample1Result.stdDev(field = "duration")
	print("stddev duration: ",stdDev1)
	# todo: count on result1 and result2
	count1=sample1Result.count()
	print("count: ",count1)
	# todo: sum on result1 and result2
	sum1=sample1Result.sum(field = "duration")
	print("sum duration: ",sum1)
	b = datetime.datetime.now ( )
	print ( "duration: ", (b - a) )

	return

if __name__ == '__main__':
	main()
