# -*- coding: utf-8 -*-
import CardClass
import CreateTables
import readFile

# Read in the json file
json = readFile.openJsonFile('AllCards-x.json')

# This line will create the initial tables from the various card properties
CreateTables.createTablesFromProperties(json)

card = CardClass.createCard(json)
card.importProperties()
