import random

def play_rock_paper_scissor():
	print("""
	===== Rock, Paper, Scissors =====
	Instructions:
	  The game goes on for 3 rounds.
	  The winner is decided after 
	  the third round.
		
	
	Scissor(0), Rock(1), Paper(2) : """)
	count = 0
	win_count = 0
	lose_count = 0
	users_choice = "0"
	computers_choice = 0
	computers_choice_str = "0"
	while True:
		if count == 3:
			break
		users_choice = input("\nChoose an option: ")	
		computers_choice = random.randint(0, 3)
		computers_choice_str = str(computers_choice)		
		if users_choice == "0":
			print("You are. Scissor. ", end='')
			count += 1
		elif users_choice == "1":
			print("You are. Rock. ", end='')
			count += 1
		elif users_choice == "2":
			print("You are. Paper. ", end='')
			count += 1
		else:
			print("Invalid input")
			continue
		if computers_choice_str == "0":
			print("Computer is. Scissor. ", end='')
		elif computers_choice_str == "1":
			print("Computer is. Rock. ", end='')
		elif computers_choice_str == "2":
			print("Computer is. Paper. ", end='')
		if computers_choice_str == users_choice:
			print("You Draw")
			count -= 1
			continue

		if(computers_choice_str == "0" and users_choice == "1") or (computers_choice_str == "1" and users_choice == "2") or (computers_choice_str == "2" and users_choice == "0"):
			print("You Win", end='')
			win_count += 1
		else:
			print("You Lose", end='')
		if count == 3:
			break
	if win_count == 2:
		print("""
		You Won, The end""")
	else:
		print("""
		You lost, The end""")
		
	






	