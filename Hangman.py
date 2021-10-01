def game():
	import random
	# import replit
	from art import HangmanStages as stages, HangmanLogo as logo
	from game_data import HangmanWordList as word_list
	chosen_word = random.choice(word_list)
	word_length = len(chosen_word)
	end_of_game = False
	lives = 6
	check = []
	display = []
	for _ in range(word_length):
		display += "_"
	print(logo)
	print("Welcome to Hangman!")
	while not end_of_game:
		# replit.clear()
		guess = input("Guess a letter: ").lower()
		if guess in check:
			print('You have already guessed this letter. Guess again')
			continue
		check.append(guess)
		for position in range(word_length):
			letter = chosen_word[position]
			if letter == guess:
				display[position] = letter
		if guess not in chosen_word:
			print(f'{guess} is not in word')
			lives -= 1
			if lives == 0:
				end_of_game = True
				print(f"You lose. The word was {chosen_word}")
		print(f"{' '.join(display)}")
		if "_" not in display:
			end_of_game = True
			print("You win.")
		print(stages[lives])
