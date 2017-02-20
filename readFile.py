import json

def openJsonFile(fileName):
	with open(fileName, 'r') as data_file:    
		data = json.load(data_file)
	return data