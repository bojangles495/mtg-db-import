class NameClass(object):
	nameList = []
	alterTableQuery = 'ALTER TABLE `name` ADD `card_name` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, nameList, model):
		self.nameList = nameList
		self.model = model

	def getList(self):
		return self.nameList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardName(self):
		self.model.alterTable(self.getAlterTableQuery())
		nameList = []
		for nameUnique in self.getList():
			if nameUnique not in nameList:
				nameList.append(nameUnique)

		for name in nameList:
			query = 'INSERT INTO `name` SET `card_name` =  "{0}";'.format(name.replace('"', '\\"'))
			self.model.insert(query)

def createName(nameList, model):
    name = NameClass(nameList, model)
    return name
