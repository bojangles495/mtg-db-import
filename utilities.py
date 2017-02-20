def generateAbstractList(dataSet, checkedProperty):
	propertyList = []
	for propertyObj in dataSet:
		if checkedProperty in dataSet[propertyObj]:
			if dataSet[propertyObj][checkedProperty] not in propertyList:
				propertyList.append(dataSet[propertyObj][checkedProperty])
	return propertyList