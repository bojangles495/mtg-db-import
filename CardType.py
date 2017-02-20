class TypeClass(object):
	typeList = []
	alterTableQuery = 'ALTER TABLE `cardType` ADD `cardType` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, typeList, model):
		self.typeList = typeList
		self.model = model

	def getList(self):
		return self.typeList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardType(self):
		self.model.alterTable(self.getAlterTableQuery())
		typeList = []
		for typeUnique in self.getList():
			query = 'INSERT INTO `cardType` SET `cardType` =  "{0}";'.format(typeUnique.replace("\u2014", " - ").replace("\u2018", "'").replace("\u2019", "'"))
			self.model.insert(query, True)

def createType(typeList, model):
    cardType = TypeClass(typeList, model)
    return cardType