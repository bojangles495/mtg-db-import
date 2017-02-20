# -*- coding: utf-8 -*-
import dbConnection

class ModelClass(object):
	def __init__(self):
		self.db = dbConnection.getConnection()

	def alterTable(self, alterStatement):
		print("Executing Query: " + alterStatement + "\n")
		db = dbConnection.getConnection()
		cur = db.cursor()
		cur.execute(alterStatement)
		cur.close()
		dbConnection.closeConnection(db)

	def insert(self, insertQuery, suppressPrintQuery = False):
		if suppressPrintQuery != True:
			print("Executing Query: " + insertQuery + "\n")
		db = dbConnection.getConnection()
		cur = db.cursor()
		cur.execute(insertQuery)
		db.commit()
		cur.close()
		dbConnection.closeConnection(db)

def create():
	model = ModelClass()
	return model
