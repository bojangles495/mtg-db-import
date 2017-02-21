class RulingsClass(object):
	propertyList = []
	alterTableQuery = 'ALTER TABLE `rulings` ADD `rulings_field` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, propertyList, model):
		self.propertyList = propertyList
		self.model = model

	def getList(self):
		return self.propertyList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardRulings(self):
		self.model.alterTable(self.getAlterTableQuery())
		propertyList = []
		# for propertyUnique in self.getList():
		# 	print(propertyUnique)

def createRulings(propertyList, model):
    cardRulings = RulingsClass(propertyList, model)
    return cardRulings