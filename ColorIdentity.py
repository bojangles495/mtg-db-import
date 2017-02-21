class ColorIdentityClass(object):
	colorIdentityList = []
	alterTableQuery = 'ALTER TABLE `colorIdentity` ADD `color_identity` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, colorIdentityList, model):
		self.colorIdentityList = colorIdentityList
		self.model = model

	def getList(self):
		return self.colorIdentityList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardColorIdentity(self):
		self.model.alterTable(self.getAlterTableQuery())
		# colorIdentityList = []
		# for colorIdentityUnique in self.getList():
		# 	print(colorIdentityUnique)

def createColorIdentity(colorIdentityList, model):
    colorIdentity = ColorIdentityClass(colorIdentityList, model)
    return colorIdentity
