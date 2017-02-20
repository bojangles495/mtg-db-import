import dbConnection

def getRootProperties(obj):
	rootPropterties = []
	for cardName, cardObj in obj.items():
		for propertyKey, propertyValue in cardObj.items():
			if propertyKey not in rootPropterties:
				rootPropterties.append(propertyKey)
	return rootPropterties

def createTablesFromProperties(dataSet):
	cardRootPropertiesList = getRootProperties(dataSet)
	queryString = ""
	tempProperty = ""
	for cardProperty in cardRootPropertiesList:
		tempProperty = cardProperty
		executionStatement = ""
		if cardProperty == 'type':
			tempProperty = "cardType"
		elif cardProperty == 'types':
			tempProperty = "cardTypes"
		executionStatement = "DROP TABLE IF EXISTS `{0}`; CREATE TABLE `{1}`(u_id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY ( u_id ));".format(tempProperty, tempProperty)
		queryString = queryString + "\n" + executionStatement

	print("Executing DB creation: " + queryString)
	db = dbConnection.getConnection()
	cur = db.cursor()
	cur.execute(queryString)
	cur.close()
	dbConnection.closeConnection(db)
