import random

def play_rock_paper_scissor():
	print("""
	===== Rock, Paper, Scissors =====
	Instructions:
	  The game goes on for 3 rounds.
	  The winner is decided after 
	  the third round or once either
	  players win twice in a row.
		
	
	Scissor(0), Rock(1), Paper(2) : """)
	loose_count = 0
	count = 0
	win_count = 0
	lose_count = 0
	users_choice = "0"
	computers_choice = 0
	computers_choice_str = "0"
	while True:
		users_choice = input("\nChoose an option: ")
		match users_choice:					
			case "0":
				print("You are. Scissor. ", end='')
				
			case "1":
				print("You are. Rock. ", end='')
				
			case "2":
				print("You are. Paper. ", end='')
				
			case _:
				print("Invalid input")
				continue
			
		computers_choice = random.randint(0, 2)
		#print(computers_choice, end='')
		computers_choice_str = str(computers_choice)
		match computers_choice_str:
			case "0":
				print("Computer is. Scissor. ", end='')
			case "1":
				print("Computer is. Rock. ", end='')
			case "2":
				print("Computer is. Paper. ", end='')

		if computers_choice_str == users_choice:
			print("You Draw")
			continue

		if(computers_choice_str == "0" and users_choice == "1") or (computers_choice_str == "1" and users_choice == "2") or (computers_choice_str == "2" and users_choice == "0"):
			print("You Win", end='')
			win_count += 1
		else:
			print("You Lose", end='')
			loose_count += 1

		if win_count == 2 or loose_count == 2:
			break

		count += 1
		if count == 3:
			break
	if win_count == 2:
		print("""
		You Won, The end""")
	else:
		print("""
		You lost, The end""")
		
	




	