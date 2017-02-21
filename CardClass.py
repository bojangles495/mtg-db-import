import utilities
import Model

import CardType
import CardTypes
import Cmc
import ColorIdentity
import Colors
import Hand
import ImageName
import Layouts
import Legalities
import Life
import Loyalty
import ManaCost
import Name
import Names
import Power
import Printings
import Rulings
import Source
import Starter
import CardSubTypes
import CardSuperTypes
import Text
import Toughness

class CardClass(object):
	model = Model.create()
	def __init__(self, dataSet):
		self.dataSet = dataSet
		
		self.cardType = CardType.createType(self.generateList('type'), self.model)
		self.cardTypes = CardTypes.createTypes(self.generateList('types'), self.model)
		self.cmc = Cmc.createCmc(self.generateList('cmc'), self.model)
		self.colorIdentity = ColorIdentity.createColorIdentity(self.generateList('colorIdentity'), self.model)
		self.colors = Colors.createColors(self.generateList('colors'), self.model)
		self.hand = Hand.createHand(self.generateList('hand'), self.model)
		self.imageName = ImageName.createImageName(self.generateList('imageName'), self.model)
		self.layouts = Layouts.createLayouts(self.generateList('layout'), self.model)
		self.legalities = Legalities.createLegalities(self.generateList('legalities'), self.model)
		self.life = Life.createLife(self.generateList('life'), self.model)
		self.loyalty = Loyalty.createLoyalty(self.generateList('loyalty'), self.model)
		self.manaCost = ManaCost.createManaCost(self.generateList('manaCost'), self.model)
		self.name = Name.createName(self.generateList('name'), self.model)
		self.names = Names.createNames(self.generateList('names'), self.model)
		self.power = Power.createPower(self.generateList('power'), self.model)
		self.printings = Printings.createPrintings(self.generateList('printings'), self.model)
		self.rulings = Rulings.createRulings(self.generateList('rulings'), self.model)
		self.source = Source.createSource(self.generateList('source'), self.model)
		self.starter = Starter.createStarter(self.generateList('starter'), self.model)
		self.cardSubTypes = CardSubTypes.createSubTypes(self.generateList('subtypes'), self.model)
		self.cardSuperTypes = CardSuperTypes.createSuperTypes(self.generateList('supertypes'), self.model)
		self.text = Text.createText(self.generateList('text'), self.model)
		self.toughness = Toughness.createToughness(self.generateList('toughness'), self.model)

	def generateList(self, typeProperty):
		cardObjTypeSpecific = utilities.generateAbstractList(self.dataSet, typeProperty)

		return cardObjTypeSpecific

	def importProperties(self):
		self.cardType.importCardType()
		self.cardTypes.importCardTypes()
		self.cmc.importCardCmc()
		self.colorIdentity.importCardColorIdentity()
		self.colors.importCardColors()
		self.hand.importCardHand()
		self.imageName.importCardImageName()
		self.layouts.importCardLayouts()
		self.legalities.importCardLegalities()
		self.life.importCardLife()
		self.loyalty.importCardLoyalty()
		self.manaCost.importCardManaCost()
		#self.name.importCardName()
		self.names.importCardNames()
		self.power.importCardPower()
		self.printings.importCardPrintings()
		self.rulings.importCardRulings()
		self.source.importCardSource()
		self.starter.importCardStarter()
		self.cardSubTypes.importCardSubTypes()
		self.cardSuperTypes.importCardSuperTypes()
		self.text.importCardText()
		self.toughness.importCardToughness()

def createCard(dataset):
    card = CardClass(dataset)
    return card

