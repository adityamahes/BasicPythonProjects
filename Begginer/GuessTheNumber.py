def game():
	import random
	from art import GuessTheNumberLogo as logo
	random_number = random.randint(1,100)
	print(logo)
	print("Welcome to 'Guess the number!'")
	print("I am thinking of a number between 1 and 100.")
	if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
		trials = 10
	else:
		trials = 5
	for trial in range(trials, 0, -1):
			print(f"You have {trial} attempts to guess the number.")
			guess = int(input("Make a guess: "))
			if guess > random_number:
				print("Too high...")
			elif guess < random_number:
				print("Too low")
			else:
				print(f"You got it! The answer was {random_number}")
				exit()
	print(f"You've run out of guesses you lose. The number was {random_number}")