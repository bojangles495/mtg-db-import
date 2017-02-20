class NamesClass(object):
	namesList = []
	alterTableQuery = 'ALTER TABLE `names` ADD `card_names` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, namesList, model):
		self.namesList = namesList
		self.model = model

	def getList(self):
		return self.namesList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardNames(self):
		self.model.alterTable(self.getAlterTableQuery())
		# This section will need some work as it its purpose is for split and flip cards ie. Odds//Ends or Bloodline Keeper/Lord of Lineage
		# namesList = []
		# for namesUnique in self.getList():
		# 	print(namesUnique)
		

def createNames(namesList, model):
    names = NamesClass(namesList, model)
    return names
