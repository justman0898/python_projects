import to_do_list

running = True
while running:
	to_do_list.display_interface()
	usersChoice = input("Choose an option: ")
	match usersChoice:
		case "1":
			in_add_task = True
			while in_add_task:
				usersChoice1 = input("Add a Task: ")
				to_do_list.add_task(usersChoice1)
				print("""
	00. Back """)		
				users_choice = input("Choose an option: ")
				match users_choice:
					case"00": 
						in_add_task = False
					case _:
						print("Enter a valid option")
						
			
		case "2":
			in_view = True
			while in_view:
				print(to_do_list.view_all_tasks(to_do_list.tasks))
				print("""
	00. Back """)		
				users_choice2 = input("Choose an option: ")
				match users_choice2:
					case"00": 
						in_view = False
					case _:
						print("Enter a valid option: ")
		case "3":
			in_mark = True
			while in_mark:
				print(to_do_list.view_all_tasks(to_do_list.tasks))
				users_choice3 = input("Choose an option: ")
				new_users_choice3 = int(users_choice3)
				to_do_list.mark_as_complete(new_users_choice3)
				print("""
	00. Back """)		
				users_choice33 = input("Choose an option: ")
				match users_choice33:
					case"00": 
						in_mark = False
					case _:
						print("Enter a valid option")
		case "4":
			in_delete = True
			while in_delete:
				print(to_do_list.view_all_tasks(to_do_list.tasks))	
				users_choice44 = input("Choose an option: ")
				new_users_choice44 = int(users_choice44)
				to_do_list.delete_task(new_users_choice44)
				print("""
	00. Back """)		
				users_choice44 = input("Choose an option: ")
				match users_choice33:
					case"00": 
						in_delete = False
					case _:
						print("Enter a valid option")

		case "5":
			running = False
		case _:
			print("Enter a valid option")		


