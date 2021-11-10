values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':11, 'queen':12,
         'king':13, 'ace':14}
import random
suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')

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

	def __init__(self, name):
		self.name = name.capitalize()
		self.hand = []

	def draw_one(self):
		return self.hand.pop(0)

	def __str__(self):
		print(f'My name is {self.name} and I have {len(self.hand)} cards')


def get_name(player):
	return input(f'Player {player} what is your name? \n')

def get_war_num():
	while(True):
		num = input('How many cards would you like to be drawn in a war? \n')

		try:
			num = int(num)
		except ValueError:
			try:
				num = values[num.lower()]
			except KeyError:
				print('I could not understand your answer, please provide a number. \n')
				continue

		if(num > 1 and num < 6):
			break
		else:
			print('Please pick a number greater than one and less than six. \n')

	return num

def play():
	main_deck = Deck()
	main_deck.shuffle()
	player_one = Player(get_name('One'))
	player_two = Player(get_name('Two'))
	war_num = get_war_num()
	game_on = True
	round_num = 0

	for x in main_deck.card_list:
		player_one.hand.append(main_deck.deal_one())
		player_two.hand.append(main_deck.deal_one())

	while(game_on):
		p1_table = []
		p1_table.append(player_one.draw_one())

		p2_table = []
		p2_table.append(player_two.draw_one())

		war = True
		round_num += 1
		print(f'ROUND {round_num}')

		while(war):
			if(p1_table[-1].value > p2_table[-1].value):
				print(f'{player_one.name} Wins\n')
				player_one.hand.extend(p1_table)
				player_one.hand.extend(p2_table)
				war = False
			elif(p1_table[-1].value < p2_table[-1].value):
				print(f'{player_two.name} Wins\n')
				player_two.hand.extend(p2_table)
				player_two.hand.extend(p1_table)
				war = False
			else:
				print('WAR!!!!')

				if(len(player_one.hand) < war_num):
					print(f'{player_one.name} was not able to declare war... \n {player_two.name} wins!!!')
					war = False
					game_on = False
				elif(len(player_two.hand) < war_num):
					print(f'{player_two.name} was not able to declare war... \n {player_one.name} wins!!!')
					war = False
					game_on = False
				else:
					for y in range(war_num):
						p1_table.append(player_one.draw_one())
						p2_table.append(player_two.draw_one())


		if(len(player_one.hand) < 1):
			print(f'{player_two.name} Has Won!')
			game_on = False
		elif(len(player_two.hand) < 1):
			print(f'{player_one.name} Has Won!')
			game_on = False
		
if(__name__ == '__main__'):
	play()




