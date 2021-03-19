import csv
import json
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

		with open(destFilePath,"w") as destFile:
			# destFile.writelines("%s\n"%x for x in data)
			json.dump(data,destFile)





if __name__ == '__main__':
	sourceFilePath="/Users/sxs2561/Desktop/imdb_dataset/name_basics_first_10k.tsv"
	destFilePath="/Users/sxs2561/Documents/AcademicAssignments/cse_541/pickledb/inputs/name_basics_first_10k.json"
	convertToJson(sourceFilePath = sourceFilePath,destFilePath = destFilePath)