Must create a <em>dbConnection.py</em> file that sets up your connection to mysql. The set up for my configuration is:

	#!/usr/bin/python
	# -*- coding: utf-8 -*-

	import MySQLdb as mdb
	import sys

	def getConnection():
		connection = mdb.connect(:server-ip, :username, :password, :database)
		return connection

	def closeConnection(dbConnection):
		if dbConnection:
			dbConnection.close()



This file is necessary because the <em>Model.py</em> and <em>CreateTables.py</em> files import <em>dbConnection.py</em>

**The source json file that I am using comes from <a href:"https://mtgjson.com/">https://mtgjson.com/</a> All Cards + Extras