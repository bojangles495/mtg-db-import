class SubTypesClass(object):
	subTypesList = []
	alterTableQuery = 'ALTER TABLE `subtypes` ADD `cardSubType` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, subtTypesList, model):
		self.subTypesList = subtTypesList
		self.model = model

	def getList(self):
		return self.subTypesList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardSubTypes(self):
		self.model.alterTable(self.getAlterTableQuery())
		subTypesList = []
		for subTypesUnique in self.getList():
			if subTypesUnique[0] == 'Lady':
				ladyString = subTypesUnique[0] + " " + subTypesUnique[1] + " " + subTypesUnique[2] + " " + subTypesUnique[3]
				subTypesList.append(ladyString)
			else:
				for subtype in subTypesUnique:
					if subtype not in subTypesList:
						subTypesList.append(subtype)
		for sub in subTypesList:
			query = 'INSERT INTO `subtypes` SET `cardSubType` =  "{0}";'.format(sub.replace("\u2018", "'").replace("\u2019", "'"))
			self.model.insert(query, True)

def createSubTypes(subTypesList, model):
    subtypes = SubTypesClass(subTypesList, model)
    return subtypes
