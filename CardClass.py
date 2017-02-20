import utilities
import Model
import Layouts
import CardSubTypes
import CardSuperTypes
import CardType
import CardTypes

class CardClass(object):
	model = Model.create()
	def __init__(self, dataSet):
		self.dataSet = dataSet
		self.layouts = Layouts.createLayouts(self.generateList('layout'), self.model)
		self.cardSubTypes = CardSubTypes.createSubTypes(self.generateList('subtypes'), self.model)
		self.cardSuperTypes = CardSuperTypes.createSuperTypes(self.generateList('supertypes'), self.model)
		self.cardType = CardType.createType(self.generateList('type'), self.model)
		self.cardTypes = CardTypes.createTypes(self.generateList('types'), self.model)

	def generateList(self, typeProperty):
		cardObjTypeSpecific = utilities.generateAbstractList(self.dataSet, typeProperty)

		return cardObjTypeSpecific
	def importProperties(self):
		self.layouts.importCardLayouts()
		self.cardSubTypes.importCardSubTypes()
		self.cardSuperTypes.importCardSuperTypes()
		self.cardType.importCardType()
		self.cardTypes.importCardTypes()

def createCard(dataset):
    card = CardClass(dataset)
    return card
