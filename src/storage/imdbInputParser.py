import csv
import json
import src.storage.fileUtility as FileUtility
def convertToJson(sourceFilePath,destFilePath):
	with open(sourceFilePath,"r") as sourceFile:
		reader=csv.DictReader(sourceFile,delimiter="\t")
		lineCount=0
		headerRow=[]
		data=[]
		for row in reader:
			if lineCount==0:
				# print("column names are ",",".join(row))
				headerRow=",".join(row).split(",")
				print(headerRow)

			rowJsonContent={}
			for headerField in headerRow:
				rowJsonContent[headerField]=row[headerField]
			# print(rowJsonContent)
			data.append(rowJsonContent)
			lineCount+=1

		# with open(destFilePath,"w") as destFile:
		# 	json.dump(data,destFile)
		FileUtility.atomicWriteToFile(filePath = destFilePath,data = data)

def currentConvertToJson(sourceFilePath, destFilePath):
	with open(sourceFilePath,"r") as sourceFile:
		reader=csv.DictReader(sourceFile,delimiter=",")
		lineCount=0
		headerRow=[]
		data=[]
		for row in reader:
			if lineCount==0:
				headerRow=",".join(row).split(",")
				print(headerRow)
			rowJsonContent={}
			for headerField in headerRow:
				rowJsonContent[headerField]=row[headerField]

			data.append(rowJsonContent)
			lineCount+=1

		for i in range(1,4):
			print(data[i])
		FileUtility.atomicWriteToFile(filePath = destFilePath,data=data)
	return





if __name__ == '__main__':
	sourceFilePath="/Users/sxs2561/Documents/OneDrive - The Pennsylvania State University/Course Work/cse_541/project/imdb_kaggle_dataset/IMDb title_principals.csv"
	destFilePath="/Users/sxs2561/Documents/OneDrive - The Pennsylvania State University/Course Work/cse_541/project/imdb_kaggle_dataset/full/jsons/imdb_title_principals.json"
	currentConvertToJson(sourceFilePath = sourceFilePath,destFilePath = destFilePath)