
from card_games import war
from two_players import tic_tac_toe as ttt
from card_games import BlackJack as bj

def do_imports():
	from Games import card_games
	from Games import two_players
	from card_games import war
	from two_players import tic_tac_toe as ttt
	from card_games import BlackJack as bj

games = {1:'Tic-Tac-Toe', 2:'War', 3:'Black Jack'}

def welcome_message():
	print('Welcome to command line games!')

def get_game():
	user_game = 'a'

	for game in games:
		print(str(game) + ' | ' + games[game])

	while(user_game not in '123'):
		user_game = input('Please pick which game you want to play using the coresponding number.\n')

	user_game = int(user_game)

	if(user_game == 1):
		ttt.play()
	elif(user_game == 2):
		war.play()
	elif(user_game == 3):
		bj.play()

def get_keep_playing():
	while(True):
		answer = input('Would you like to play another game?\n')
		if(answer.lower() == 'yes'):
			return True
		elif(answer.lower() == 'no'):
			return False
		else:
			print('I could not understand you answer. Please put yes or no as your answer.\n')

def main_loop():
	keep_going = True
	while(keep_going == True):
		welcome_message()
		get_game()
		keep_going = get_keep_playing()

if(__name__ == '__main__'):
	main_loop()