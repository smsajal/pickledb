from src.storage.tempResult import TempResult as TempResult


'''
	args:
		tempResult1 = table1 for the join
		joinField1 = field from table1 used for join
		tempResult2 = table2 for the join
		joinField2 = field from table2 used for join
'''
def nestedLoopJoin(tempResult1, joinField1, tempResult2, joinField2):
	data=[]
	for row1 in tempResult1.getData():
		for row2 in tempResult2.getData():
			if row1[joinField1]==row2[joinField2]:
				data.append(row1.update(row2))
	return TempResult(data = data)


def hashJoin(tempResult1, joinField1, tempResult2, joinField2):

	data=[]

	# get the smaller and bigger dataset
	smallerTempResult=None
	biggerTempResult=None
	if tempResult1.count()<tempResult2.count():
		smallerTempResult=tempResult1
		biggerTempResult=tempResult2
	else:
		smallerTempResult=tempResult2
		biggerTempResult=tempResult1

	smallerMap= {}
	for x in smallerTempResult.getData():
		smallerMap[x[joinField1]]=x

	for x in biggerTempResult.getData():
		if x[joinField2] in smallerMap:
			data.append(x.update(smallerMap[x[joinField2]]))


	return TempResult(data = data)


def sortedMergeJoin(tempResult1, joinField1, tempResult2, joinField2):

	data=[]

	sortedTempResult1Data=sorted(tempResult1.getData(), key=lambda i:i[joinField1])
	sortedTempResult2Data=sorted(tempResult2.getData(),key = lambda i:i[joinField2])

	data1Count=len(sortedTempResult1Data)
	data2Count=len(sortedTempResult2Data)
	i=0
	j=0
	while i<data1Count and j<data2Count:
		row1=sortedTempResult1Data[i]
		row2=sortedTempResult2Data[j]
		if row1[joinField1]==row2[joinField2]:
			data.append(row1.update(row2))
			j+=1
		else:
			i+=1

	return TempResult(data = data)