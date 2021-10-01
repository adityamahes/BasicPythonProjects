def game():
	import art
	import random
	from game_data import HigherLowerData as data
	# from replit import clear
	user_continue = True
	score = 0
	candidate = random.choice(data)
	candidat = random.choice(data)
	while user_continue:
		print(art.HigherLowerLogo)
		print(f'Compare A: {candidate["name"]}, a {candidate["description"]}, from {candidate["country"]}\n', art.HigherLowerVs, f'\nCompare B: {candidat["name"]}, a {candidat["description"]}, from {candidat["country"]}')
		if candidate['follower_count'] > candidat['follower_count']:
			answer = "a"
		else:
			answer = "b"
		choice = input("Who has more followers? Type 'A' or 'B': ").lower()
		if choice == answer:
			score += 1
			candidate = candidat
			candidat = random.choice(data)
			# clear()
			print(f"Your Right! Current Score: {score}")
		else:
			# clear()
			print(f"Sorry that's wrong. Score: {score}")
			user_continue = False
