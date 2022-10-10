def game():
	import random
	from art import RockPaperScissorsRock as rock, RockPaperScissorsPaper as paper, RockPaperScissorScissors as scissors, RockPaperScissorsLogo as logo
	print(logo)
	gestures = [rock, paper, scissors]
	ifcontinue = True
	while ifcontinue:
		choice = int(input('What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n'))
		computerchoice = random.randint(0,2)

		if (choice > 2 or choice < 0) or (computerchoice > 2 or computerchoice < 0):
			print('Invalid Input you Lose')
		else:
			print(gestures[choice])
			print(f'Computer choses {gestures[computerchoice]}')
			if computerchoice == 0 and choice == 1:
				print('You Win')
			elif computerchoice == 0 and choice == 2:
				print('You lose')
			elif computerchoice == 1 and choice == 2:
				print('You Win')
			elif computerchoice == 1 and choice == 0:
				print('You lose')
			elif computerchoice == 2 and choice == 0:
				print('You Win')
			elif computerchoice == 2 and choice == 1:
				print('You lose')
			else:
				print('Draw!')
			if input("Do you want to play another round (y,n)? : ") == 'n':
				ifcontinue = False
				print("Goodbye")