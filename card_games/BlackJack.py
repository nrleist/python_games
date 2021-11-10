import random

values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10,
         'king':10, 'ace':None}
suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
colors = {'white':1, 'red':3, 'blue':5}


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit.lower()
        self.rank = rank.lower()
        self.value = values[rank.lower()]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    
    def __init__(self):
        
        self.card_list = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)               
                self.card_list.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.card_list)
        
    def deal_one(self):
        return self.card_list.pop()


class Player:

	def __init__(self, deck, name = 'dealer', is_dealer = False):
		self.name = name.capitalize()
		self.is_dealer = is_dealer
		self.hand = []
		self.deck = deck

	def getAceValue(self):
		while(True):
			answerValue = input('Would you like this card to be worth 1 or 14?\n')
			try:
				answerValue = int(answerValue)
			except:
				print('I could not understand your answer. Please input a number.')
				continue

			if(not(answerValue == 14 or answerValue == 1)):
				print('Please put either 1 or 14 as your answer.')
			else:
				break
		return answerValue

	def draw_one(self):
		cardDrawn = self.deck.deal_one()
		if(cardDrawn.value == None):
			if(self.is_dealer == True):
				cardDrawn.value = 1
			else:
				cardDrawn.value = self.getAceValue()

		self.hand.append(cardDrawn)

	def getHandValue(self):
		handValue = 0
		for card in self.hand:
			handValue += card.value
		return handValue

	def printCardsHand(self):
		indexCount = 0
		cards_on_table = ''
		for card in self.hand:
			cards_on_table += f' {self.hand[indexCount].rank}({self.hand[indexCount].value}) |'
			indexCount += 1

		print(cards_on_table + f' TOTAL-{self.getHandValue()}')

	def getHitOrStop(self):
		while(True):
			hit_or_stop = input('Would you like to draw another card or stop?\nType hit to draw another or type stop to stop.\n')

			if(hit_or_stop.lower() == 'hit'):
				returnVal = True
				break
			elif(hit_or_stop.lower() == 'stop'):
				returnVal = False
				break
			else:
				print('I could not understand your answer. Please type hit or stop.')
		return returnVal

	def checkBust(self):
		if(self.getHandValue() > 21):
			if(not(self.is_dealer)):
				self.printCardsHand()
				print('Whoops, looks like you went over 21')
			return True
		else:
			return False

	def playRound(self):
		self.hand = []
		has_busted = False
		self.draw_one()
		self.draw_one()
		self.printCardsHand()
		while(self.getHitOrStop()):
			self.draw_one()
			if(self.checkBust()):
				has_busted = True
				break
			elif(self.getHandValue() == 21):
				print(self.printCardsHand())
				break
			else:
				self.printCardsHand()

		if(has_busted):
			return 0
		else:
			return self.getHandValue()

	def doDealer(self, playerNum):
		has_busted = False
		if(self.is_dealer == True):
			self.hand = []
			while(True):
				self.draw_one()
				if(self.checkBust()):
					has_busted = True
					break
				elif(self.getHandValue() > playerNum):
					break
				elif(self.getHandValue() == 21):
					break
			if(has_busted):
				return 0
			else:
				return self.getHandValue()
		else:
			raise Exception("Func doDealer() called on player type")

	def __str__(self):
		print(f'My name is {self.name} and I have {len(self.hand)} cards')


class Chip:

	def __init__(self, color):
		self.color = color.lower()
		self.worth = colors[self.color]


class Bank:

	def __init__(self):
		self.chips = []

		for a in range(3):
			self.chips.append(Chip('blue'))
		for b in range(3):
			self.chips.append(Chip('red'))
		for c in range(6):
			self.chips.append(Chip('white'))

	def deposit(self, money):
		for chip in money:
			self.chips.append(chip)

	def getWhiteChips(self):
		chipList = []
		for chip in self.chips:
			if(chip.color == 'white'):
				chipList.append(chip)
		return chipList

	def getRedChips(self):
		chipList = []
		for chip in self.chips:
			if(chip.color == 'red'):
				chipList.append(chip)
		return chipList

	def getBlueChips(self):
		chipList = []
		for chip in self.chips:
			if(chip.color == 'blue'):
				chipList.append(chip)
		return chipList

	def getValue(self):
		chipsValue = 0
		for chip in self.chips:
			chipsValue += chip.worth
		return chipsValue

	def splitChips(self, nums):
		if(nums[2] > self.getWhiteChipsChips()):
			pass
		if(nums[1] > self.getRedChips()):
			pass

	def countChipsNeeded(self, amount):
		blueChips, redChips, whiteChips = 0, 0, 0
		blueChips = int(amount / 5)
		redChips = int((amount % 5) / 3)
		whiteChips = int((amount % 5) % 3) 
		return (blueChips, redChips, whiteChips)

	def getNeededChips(self, nums):
		withdrawalList = []
		popList = []

		count = 0
		indexCount = 0
		while(True):
			if(count < nums[0]):
				if(self.chips[indexCount].color == 'blue'):
					withdrawalList.append(self.chips[indexCount])
					self.chips.pop(indexCount)
					count += 1
				else:
					indexCount += 1
			else:
				break

		count = 0
		indexCount = 0
		while(True):
			if(count < nums[1]):
				if(self.chips[indexCount].color == 'red'):
					withdrawalList.append(self.chips[indexCount])
					self.chips.pop(indexCount)
					count += 1
				else:
					indexCount += 1
			else:
				break

		count = 0
		indexCount = 0
		while(True):
			if(count < nums[2]):
				if(self.chips[indexCount].color == 'white'):
					withdrawalList.append(self.chips[indexCount])
					self.chips.pop(indexCount)
					count += 1
				else:
					indexCount += 1
			else:
				break

		return withdrawalList

	def withdrawal(self, amount):
		if(amount == self.getValue()):
			returnList = self.chips
			self.chips = []
			return returnList
		else:
			return self.getNeededChips(self.countChipsNeeded(amount)) 

	def __str__(self):
		return f'You have {len(self.getWhiteChips())} white chips, {len(self.getRedChips())} red chips and {len(self.getBlueChips())} blue chips for a value of {self.getValue()}'


def getPlayerName():
	return input('Hello, thank you for playing Black Jack.\nPlease enter your name...\n').capitalize()

def explainRules(name, Bank):
	print(f'\nWelcome to Black Jack, {name}. Here are the rules...\n\n1) You will begin with {Bank.__str__()[10::]}\n2) For each card you can either pick to draw another or stop.\n3) The goal is to get closest to 21 with out going over.\n4)White Chips are worth 1, Red worth 3 and Blue worth 5.\n5)If an ace is drawn you can pick if it adds 1 or 14 to the total value of the cards.\nGood Luck!!!\n')
	
def getBet(playerBank):
	betList = []
	while(True):
		bet = input('Please type your bet...\n')		
		try:
			bet = int(bet)
		except:
			print('I could not understand your answer. Please input a number.')
			continue

		if(bet > playerBank.getValue()):
			print(f"You don't have enough money to place that bet, please type a number that is less than or equal to {playerBank.getValue()}")
		elif(bet < 1):
			print('Please pick a number that is one or greater.')
		else:
			break

	betList = playerBank.withdrawal(bet)
	return betList

def getBetValue(chips):
	chipsValue = 0
	for chip in chips:
		chipsValue += chip.worth
	return chipsValue

def getWinner(playerNum, dealerNum):
	if(playerNum > dealerNum):
		print('You have won this round!!!')
		return True
	elif(playerNum == dealerNum):
		print('It was a tie!')
		return None
	elif(playerNum < dealerNum):
		print('The dealer has won')
		return False

def addMoney(playerBank, bet, win):
	depositList = bet
	if(win == True):
		depositList += depositList
		print(f'Congratulations you just earned {getBetValue(bet)} worth of chips!!!')
		playerBank.deposit(depositList)
	elif(win == None):
		print("You did not win or lose any money!")
		playerBank.deposit(bet)
	elif(win == False):
		print(f'You just lost {getBetValue(bet)} worth of chips.')

def askKeepGoing(playerBank):
	while(True):
		answer = input(f'Would you like to play another round or walk away with {playerBank.getValue()} worth of chips?\nType yes to play another round and type no to quit.\n')
		if(answer.lower() == 'yes'):
			return True
			break
		elif(answer.lower() == 'no'):
			return False
			break
		else:
			print('I could not understand your answer. Please type yes or no')

def gamePlayLoop(name):
	roundNum = 1
	keepPlaying = True
	while(keepPlaying):
		if(roundNum == 1):
			mainDeck = Deck()
			mainDeck.shuffle()
			playerBank = Bank()
			playerHand = Player(mainDeck, name)
			dealer = Player(mainDeck, is_dealer = True)
			explainRules(name, playerBank)

		print(f'Round #{roundNum}')
		print(playerBank)
		playerBet = getBet(playerBank)
		playerNum = playerHand.playRound()
		dealerNum = dealer.doDealer(playerNum)
		has_won = getWinner(playerNum, dealerNum)
		addMoney(playerBank, playerBet, has_won)
		
		if(playerBank.getValue() == 0):
			keepPlaying = False
		else:
			keepPlaying = askKeepGoing(playerBank)
		roundNum += 1

	print(f'Thank You for playing Black Jack!\nYou are walking away with {playerBank.getValue()} worth of chips!')

def play():
	gamePlayLoop(getPlayerName())

if(__name__ == '__main__'):
	play()




