import utilities
import Model
import CardSubTypes
import CardSuperTypes
import CardType
import CardTypes
import Colors
import Layouts

class CardClass(object):
	model = Model.create()
	def __init__(self, dataSet):
		self.dataSet = dataSet
		
		self.cardSubTypes = CardSubTypes.createSubTypes(self.generateList('subtypes'), self.model)
		self.cardSuperTypes = CardSuperTypes.createSuperTypes(self.generateList('supertypes'), self.model)
		self.cardType = CardType.createType(self.generateList('type'), self.model)
		self.cardTypes = CardTypes.createTypes(self.generateList('types'), self.model)
		self.colors = Colors.createColors(self.generateList('colors'), self.model)
		self.layouts = Layouts.createLayouts(self.generateList('layout'), self.model)

	def generateList(self, typeProperty):
		cardObjTypeSpecific = utilities.generateAbstractList(self.dataSet, typeProperty)

		return cardObjTypeSpecific
	def importProperties(self):
		
		self.cardSubTypes.importCardSubTypes()
		self.cardSuperTypes.importCardSuperTypes()
		self.cardType.importCardType()
		self.cardTypes.importCardTypes()
		self.colors.importCardColors()
		self.layouts.importCardLayouts()

def createCard(dataset):
    card = CardClass(dataset)
    return card
