import random
import string
import json
import os
def generateRandomString(stringLength):
	choiceCharacters=string.ascii_letters+string.digits
	result_str = ''.join ( random.choice ( choiceCharacters ) for i in range ( stringLength ) )
	return result_str

def readJsonFile(filePath):
	with open(filePath,"r") as jsonFile:
		data=json.load(jsonFile)

	return data

def atomicWriteToFile(filePath,data):
	tempfilePath=filePath+".tmp"
	with open(tempfilePath,"w") as tempFile:
		json.dump(data,tempFile)
		try:
			os.remove(filePath)
		except OSError:
			pass
		os.rename(tempfilePath,filePath)
	return

def writeToJsonFile(filePath,data):
	with open(filePath,"w") as outfile:
		json.dump(data,outfile)
	return

if __name__ == '__main__':
	sourceFile="/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/inputs/atomic_tester_data.json"
	x=readJsonFile(sourceFile)
	x.extend([{'name': 'd4', 'age': 40}])
	# print(x)
	atomicWriteToFile(sourceFile,x)