question_1 = input("What is your problem?: ");

question_2 = input("Have you had this problem before(yes or no)?: ").lower();

match question_2:
	case "yes":
		print("Well, you have it again.")
	case "no":
		print("Well, you have it now")
	case _:
		print("Unknown command")