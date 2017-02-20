class LayoutsClass(object):
	layoutsList = []
	alterTableQuery = 'ALTER TABLE `layout` ADD `layout_type` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci NOT NULL AFTER `u_id`;'

	def __init__(self, layoutsList, model):
		self.layoutsList = layoutsList
		self.model = model

	def getList(self):
		return self.layoutsList

	def getAlterTableQuery(self):
		return self.alterTableQuery

	def importCardLayouts(self):
		self.model.alterTable(self.getAlterTableQuery())
		for layout in self.getList():
			query = 'INSERT INTO `layout` SET `layout_type` =  "{0}";'.format(layout)
			self.model.insert(query, True)

def createLayouts(layoutsList, model):
    layouts = LayoutsClass(layoutsList, model)
    return layouts