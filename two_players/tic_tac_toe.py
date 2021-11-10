

def get_selection(p_turn, list, name):
	good_sel = False

	while(good_sel == False):

		try:
			sel = int(input(f'{name} please make your selection.\n'))
		except:
			print("I couldn't understand your selection.\nPlease make a selection from 1 to 9.\n \n")
		else:
			if(sel < 1 or sel > 9):
				print("Your selection was not a number 1 to 9.\nPlease make a selection from 1 to 9.\n \n")
			elif(list[sel - 1] in ['O', 'X']):
				print('That spot is already taken. Please pick an open spot. \n')
			else:
				good_sel = True

	return sel


def print_bord(bord):
	print(f'| 1 | 2 | 3 |\n| {bord[0]} | {bord[1]} | {bord[2]} |\n|   |   |   |\n-------------\n| 4 | 5 | 6 |\n| {bord[3]} | {bord[4]} | {bord[5]} |\n|   |   |   |\n-------------\n| 7 | 8 | 9 |\n| {bord[6]} | {bord[7]} | {bord[8]} |\n|   |   |   |\n')

def mark_bord(sel, bord, turn):
	new_sel = sel - 1
	
	if(turn == 1):
		bord[new_sel] = p1_let
	else:
		bord[new_sel] = p2_let
	return bord

def flip_turn(turn):
	if(turn == 1):
		return 2
	else:
		return 1

def get_current_name(turn):
	if(turn == 1):
		return p1_name
	else:
		return p2_name

def check_win(bord, turn):
	if(turn == 1):
		letter = p1_let
	else:
		letter = p2_let

	if(check_horisontal(bord, letter) or check_vertical(bord, letter) or check_diags(bord, letter)):
		return True
	else: 
		return False

def check_horisontal(bord, let):
	if(bord[0] == let and bord[1] == let and bord[2] == let):
		return True
	elif(bord[3] == let and bord[4] == let and bord[5] == let):
		return True
	elif(bord[6] == let and bord[7] == let and bord[8] == let):
		return True
	else:
		return False

def check_vertical(bord, let):
	if(bord[0] == let and bord[3] == let and bord[6] == let):
		return True
	elif(bord[1] == let and bord[4] == let and bord[7] == let):
		return True
	elif(bord[2] == let and bord[5] == let and bord[8] == let):
		return True
	else:
		return False

def check_diags(bord, let):
	if(bord[0] == let and bord[4] == let and bord[8] == let):
		return True
	elif(bord[2] == let and bord[4] == let and bord[6] == let):
		return True
	else:
		return False

def who_goes_first():
	choise = input(f'{p1_name} would you like to go first?\n')

	if(choise[0].lower() == 'y'):
		return 2
	else:
		return 1

def x_and_o():
	global p1_let
	global p2_let

	while(True):
		choise = input(f"{p2_name} would you like to be X's or O's?\n")

		if(choise[0].upper() == 'X'):
			p1_let = 'O' 
			p2_let = 'X'
			break
		elif(choise[0].upper() == 'O'):
			p1_let = 'X' 
			p2_let = 'O'
			break
		else:
			print("I could not understand your answer. Please put X or O as your answer.\n")


def game_play_loop():
	bord_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	p_turn = who_goes_first()
	x_and_o()
	has_won = False
	turn_num = 0

	while(has_won == False and turn_num < 9):
		p_turn = flip_turn(p_turn)
		player_name = get_current_name(p_turn)
		print_bord(bord_list)
		selection = get_selection(p_turn, bord_list, player_name)	
		bord_list = mark_bord(selection, bord_list, p_turn)
		turn_num += 1
		has_won = check_win(bord_list, p_turn)
		
	print_bord(bord_list)
	if has_won == True:
		print(f'Congratulations!!! {player_name} has won!!!\n')
	else:
		print('It was a draw.\n')

def ask_keep_playing():
	answer = input("Would you like to play another game?\n")

	if(answer[0].lower() == 'y'):
		return True
	else:
		return False

def get_names():
	global p1_name
	global p2_name
	p1_name = input("Player 1 what is your name?\n")
	p2_name = input("Player 2 what is your name?\n")


def play():
	keep_playing = True
	get_names()

	while(keep_playing):
		game_play_loop()
		keep_playing = ask_keep_playing()


if(__name__ == "__main__"):
	play()

