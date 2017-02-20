class SuperTypesClass(object):
	superTypesList = []
	alterTableQuery = 'ALTER TABLE `supertypes` ADD `cardSuperType` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, superTypesList, model):
		self.superTypesList = superTypesList
		self.model = model

	def getList(self):
		return self.superTypesList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardSuperTypes(self):
		self.model.alterTable(self.getAlterTableQuery())
		superTypesList = []
		for superTypesUnique in self.superTypesList:
			for supertype in superTypesUnique:
				if supertype not in superTypesList:
					superTypesList.append(supertype)
		for sup in superTypesList:
			query = 'INSERT INTO `supertypes` SET `cardSuperType` =  "{0}";'.format(sup)
			self.model.insert(query, True)

def createSuperTypes(superTypesList, model):
    supertypes = SuperTypesClass(superTypesList, model)
    return supertypes