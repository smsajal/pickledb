import random
import string
import json
def generateRandomString(stringLength):
	choiceCharacters=string.ascii_letters+string.digits
	result_str = ''.join ( random.choice ( choiceCharacters ) for i in range ( stringLength ) )
	return result_str

def readJsonFile(filePath):
	with open(filePath,"r") as jsonFile:
		data=json.load(jsonFile)

	return data

if __name__ == '__main__':
	x=readJsonFile("/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/inputs/name_basics.json")
	print(x)