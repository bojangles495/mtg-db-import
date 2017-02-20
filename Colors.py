class ColorsClass(object):
	colorsList = []
	alterTableQuery = 'ALTER TABLE `colors` ADD `color_name` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, colorsList, model):
		self.colorsList = colorsList
		self.model = model

	def getList(self):
		return self.colorsList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardColors(self):
		self.model.alterTable(self.getAlterTableQuery())
		colorsList = []
		for colorsUnique in self.getList():
			for color in colorsUnique:
				if color not in colorsList:
					colorsList.append(color)
		for color in colorsList:
			query = 'INSERT INTO `colors` SET `color_name` =  "{0}";'.format(color)
			self.model.insert(query, True)

def createColors(colorsList, model):
    colors = ColorsClass(colorsList, model)
    return colors
