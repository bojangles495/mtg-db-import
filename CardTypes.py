class TypesClass(object):
	typesList = []
	alterTableQuery = 'ALTER TABLE `cardTypes` ADD `cardTypes` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, typesList, model):
		self.typesList = typesList
		self.model = model

	def getList(self):
		return self.typesList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardTypes(self):
		self.model.alterTable(self.getAlterTableQuery())
		typesList = []
		for typesUnique in self.getList():
			if typesUnique[0] == 'Scariest':
				typesList.append(typesUnique[0] + " " + typesUnique[1] + " " + typesUnique[2] + " " + typesUnique[3] + " " + typesUnique[4])
			else:
				for typeObj in typesUnique:
					if typeObj not in typesList:
						typesList.append(typeObj)
		for cTypes in typesList:
			query = 'INSERT INTO `cardTypes` SET `cardTypes` =  "{0}";'.format(cTypes)
			self.model.insert(query, True)

def createTypes(typesList, model):
    cardTypes = TypesClass(typesList, model)
    return cardTypes